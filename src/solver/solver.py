import subprocess
import itertools
import re

from core.models import (
    Step, Group, Remove, Method,
    StepResult, SolveResult,
)
from core.rotation import (
    parse_rotation,
    remap_moves,
    remap_constraint_lines,
    inverse_face_map,
    orientation_rotation_string,
    orientation_face_map,
    identity_orientation_index,
    _ALL_24,
    _freeze,
    _MAP_TO_IDX,
    _compose,
)
from core.cache import load_cache, append_cache

import random as _random

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DEBUG = False
TIMEOUT = 1000
CACHE_TIMEOUT = 0.01
ENABLE_QUICK_OUT = True
QUICK_OUT_FACTOR = 2


# ---------------------------------------------------------------------------
# Group ordering strategies
# ---------------------------------------------------------------------------

def _remaining(group, done):
    return [s for s in group.steps if s.name not in done]

def _order_in_order(group, done):
    rem = _remaining(group, done)
    return [rem[0]] if rem else []

def _order_random(group, done):
    rem = _remaining(group, done)
    _random.shuffle(rem)
    return rem

def _evaluate_sequence(runner, steps, group, accumulated_constraints,
                        scramble, accumulated_solution):
    state = accumulated_solution
    total = 0
    solutions = []
    for step in steps:
        sol = runner._run_step(
            step=step,
            extra_directives=group.directives,
            accumulated_constraints=accumulated_constraints,
            scramble=scramble,
            accumulated_solution=state,
        )
        if sol is None:
            return None, None
        total += len(sol.split()) if sol.strip() else 0
        state = MethodRunner._join_moves(state, sol)
        solutions.append(sol)
    return total, solutions

def _order_optimal(group, done, runner, accumulated_constraints,
                   scramble, accumulated_solution, n, pick_worst):
    rem = _remaining(group, done)
    if not rem:
        return []
    batch = min(n, len(rem))
    best_seq = None
    best_score = None
    for perm in itertools.permutations(rem, batch):
        score, _ = _evaluate_sequence(
            runner, list(perm), group,
            accumulated_constraints, scramble, accumulated_solution
        )
        if score is None:
            continue
        if (best_score is None
                or (pick_worst and score > best_score)
                or (not pick_worst and score < best_score)):
            best_score = score
            best_seq = list(perm)
    return best_seq if best_seq is not None else rem[:batch]


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

class MethodRunner:
    def __init__(self, solver_path: str, workspace_root: str, timeout=TIMEOUT):
        self.solver_path = solver_path
        self.workspace_root = workspace_root
        self.timeout = timeout
        self.method_name = "unknown"

    # ── public entry point ──────────────────────────────────────────────────

    def run(self, method: Method, scramble: str) -> SolveResult:
        self.method_name = method.name
        original_scramble = scramble
        accumulated_solution = ""
        accumulated_constraints = []
        step_results = []

        # Step 1: symmetry orientation selection
        selected_rotation_str = method.rotation_str

        if method.symmetry_orientations:
            selected_rotation_str = self._select_orientation(
                method=method,
                scramble=scramble,
                base_rotation_str=method.rotation_str,
                accumulated_constraints=accumulated_constraints,
            )

        # Step 2: apply rotation to scramble
        if selected_rotation_str:
            if DEBUG:
                print(f"[ROT] Applying rotation '{selected_rotation_str}'.")
            self._active_face_map = parse_rotation(selected_rotation_str)
            scramble = remap_moves(scramble, self._active_face_map)
        else:
            self._active_face_map = None

        # Step 3: solve each item
        for item in method.items:

            if isinstance(item, Remove):
                before = len(accumulated_constraints)
                if item.command == "ALL":
                    accumulated_constraints = []
                else:
                    accumulated_constraints = [
                        c for c in accumulated_constraints if c != item.command
                    ]
                if DEBUG:
                    print(f"[REMOVE] '{item.command}' — removed {before - len(accumulated_constraints)} instance(s)")
                continue

            if isinstance(item, Step):
                solution = self._run_step(
                    step=item,
                    extra_directives=[],
                    accumulated_constraints=accumulated_constraints,
                    scramble=scramble,
                    accumulated_solution=accumulated_solution,
                )
                if solution is None:
                    print(f"[ERROR] Step '{item.name}' failed. Aborting.")
                    return SolveResult(
                        scramble=original_scramble,
                        orientation=selected_rotation_str,
                        steps=step_results,
                        failed=True,
                    )
                step_results.append(StepResult(name=item.name, solution=solution))
                accumulated_constraints.extend(item.constraints)
                accumulated_solution = self._join_moves(accumulated_solution, solution)

            elif isinstance(item, Group):
                result = self._run_group(
                    group=item,
                    accumulated_constraints=accumulated_constraints,
                    scramble=scramble,
                    accumulated_solution=accumulated_solution,
                )
                if result is None:
                    return SolveResult(
                        scramble=original_scramble,
                        orientation=selected_rotation_str,
                        steps=step_results,
                        failed=True,
                    )
                group_step_results, new_constraints, accumulated_solution = result
                step_results.extend(group_step_results)
                accumulated_constraints.extend(new_constraints)

        return SolveResult(
            scramble=original_scramble,
            orientation=selected_rotation_str,
            steps=step_results,
        )

    # ── symmetry orientation selection ──────────────────────────────────────

    def _select_orientation(self, method, scramble, base_rotation_str,
                             accumulated_constraints) -> str:
        top_items = [i for i in method.items if isinstance(i, (Step, Group))]
        eval_items = top_items[: method.symmetry_depth]

        best_rot_str = base_rotation_str
        best_score = None

        for ori_idx in method.symmetry_orientations:
            if base_rotation_str:
                base_map = parse_rotation(base_rotation_str)
                sym_map  = orientation_face_map(ori_idx)
                combined_map = _compose(base_map, sym_map)
                key = _freeze(combined_map)
                if key not in _MAP_TO_IDX:
                    continue
                combined_rot_str = orientation_rotation_string(_MAP_TO_IDX[key])
            else:
                combined_rot_str = orientation_rotation_string(ori_idx)
                combined_map = orientation_face_map(ori_idx)

            candidate_scramble = remap_moves(scramble, combined_map)
            total_moves = 0
            acc_constraints = list(accumulated_constraints)
            acc_solution = ""
            ok = True

            for item in eval_items:
                if isinstance(item, Step):
                    sol = self._run_step(
                        step=item, extra_directives=[],
                        accumulated_constraints=acc_constraints,
                        scramble=candidate_scramble,
                        accumulated_solution=acc_solution,
                    )
                    if sol is None:
                        ok = False; break
                    total_moves += len(sol.split()) if sol.strip() else 0
                    acc_solution = self._join_moves(acc_solution, sol)
                    acc_constraints.extend(item.constraints)

                elif isinstance(item, Group):
                    for step in item.steps:
                        sol = self._run_step(
                            step=step, extra_directives=item.directives,
                            accumulated_constraints=acc_constraints,
                            scramble=candidate_scramble,
                            accumulated_solution=acc_solution,
                        )
                        if sol is None:
                            ok = False; break
                        total_moves += len(sol.split()) if sol.strip() else 0
                        acc_solution = self._join_moves(acc_solution, sol)
                        acc_constraints.extend(item.directives)
                        acc_constraints.extend(step.constraints)
                    if not ok:
                        break

            if not ok:
                continue

            if DEBUG:
                print(f"[SYM] Orientation {ori_idx:2d} ({combined_rot_str or 'identity':10s}) → {total_moves} moves")

            if best_score is None or total_moves < best_score:
                best_score = total_moves
                best_rot_str = combined_rot_str

        if DEBUG:
            print(f"[SYM] → Selected: {best_rot_str or 'identity'!r} ({best_score} moves)")

        return best_rot_str

    # ── group execution ──────────────────────────────────────────────────────

    def _run_group(self, group, accumulated_constraints, scramble, accumulated_solution):
        done = set()
        group_step_results = []
        new_constraints = []

        while True:
            effective_constraints = accumulated_constraints + new_constraints
            batch = self._next_batch(
                group=group, done=done,
                accumulated_constraints=effective_constraints,
                scramble=scramble,
                accumulated_solution=accumulated_solution,
            )
            if not batch:
                break

            for step in batch:
                solution = self._run_step(
                    step=step,
                    extra_directives=group.directives,
                    accumulated_constraints=accumulated_constraints + new_constraints,
                    scramble=scramble,
                    accumulated_solution=accumulated_solution,
                )
                if solution is None:
                    print(f"[ERROR] Step '{step.name}' (group '{group.name}') failed. Aborting.")
                    return None

                group_step_results.append(StepResult(name=step.name, solution=solution))
                new_constraints.extend(group.directives)
                new_constraints.extend(step.constraints)
                accumulated_solution = self._join_moves(accumulated_solution, solution)
                done.add(step.name)

        return group_step_results, new_constraints, accumulated_solution

    def _next_batch(self, group, done, accumulated_constraints, scramble, accumulated_solution):
        order = group.order
        if order == "in_order":
            return _order_in_order(group, done)
        if order == "random":
            return _order_random(group, done)
        ctx = dict(runner=self, accumulated_constraints=accumulated_constraints,
                   scramble=scramble, accumulated_solution=accumulated_solution)
        m = re.fullmatch(r'best(?:_(\d+))?', order)
        if m:
            n = int(m.group(1)) if m.group(1) else len(group.steps)
            return _order_optimal(group, done, n=n, pick_worst=False, **ctx)
        m = re.fullmatch(r'worst(?:_(\d+))?', order)
        if m:
            n = int(m.group(1)) if m.group(1) else len(group.steps)
            return _order_optimal(group, done, n=n, pick_worst=True, **ctx)
        raise ValueError(f"Unhandled group order '{order}'")

    # ── solver call ──────────────────────────────────────────────────────────

    def _run_solver(self, step, extra_directives, accumulated_constraints,
                    current_state, timeout=None):
        effective_timeout = timeout if timeout is not None else self.timeout
        fm = getattr(self, '_active_face_map', None)
        def _rc(lines_in):
            return remap_constraint_lines(lines_in, fm) if fm else list(lines_in)

        lines = ["init_empty_cube"]
        lines.extend(_rc(accumulated_constraints))
        lines.extend(_rc(extra_directives))
        lines.extend(_rc(step.constraints))
        lines.append(current_state)
        lines.append("solve")
        solver_input = "\n".join(lines) + "\n"

        if DEBUG:
            print(f"\n===== SOLVER CALL: {step.name} =====")
            print(solver_input)

        try:
            result = subprocess.run(
                [self.solver_path, "--silent", "-n", "1"],
                input=solver_input, text=True, capture_output=True,
                cwd=".", timeout=effective_timeout,
            )
        except subprocess.TimeoutExpired:
            if DEBUG or timeout is None:
                print(f"[TIMEOUT] Step '{step.name}' exceeded {effective_timeout}s.")
            return None

        if result.returncode != 0:
            err = result.stderr.strip() or result.stdout.strip()
            print(f"[SOLVER ERROR] Step '{step.name}': {err}")
            return None

        return [l.strip() for l in result.stdout.splitlines() if l.strip()]

    def _check_already_solved(self, step, extra_directives, accumulated_constraints,
                               current_state) -> bool:
        fm = getattr(self, '_active_face_map', None)
        def _rc(lines_in):
            return remap_constraint_lines(lines_in, fm) if fm else list(lines_in)

        lines = ["init_empty_cube"]
        lines.extend(_rc(accumulated_constraints))
        lines.extend(_rc(extra_directives))
        lines.extend(_rc(step.constraints))
        lines.append(current_state)
        lines.append("solve")
        solver_input = "\n".join(lines) + "\n"

        try:
            result = subprocess.run(
                [self.solver_path, "-d", "1", "-n", "1"],
                input=solver_input, text=True, capture_output=True,
                cwd=".", timeout=CACHE_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            return False

        combined = result.stdout + result.stderr
        already_solved = "Already solved" in combined
        if DEBUG and already_solved:
            print(f"[CACHE CHECK] Already solved detected.")
        return already_solved

    # ── alg cache lookup ─────────────────────────────────────────────────────

    def _try_cache(self, step, extra_directives, accumulated_constraints,
                   scramble, accumulated_solution):
        if not step.cache_alg or not step.free_layers:
            return None
        cached_algs = load_cache(self.workspace_root, self.method_name, step.name)
        if not cached_algs:
            return None

        if DEBUG:
            print(f"[CACHE] Trying {len(cached_algs)} cached alg(s) for '{step.name}'")

        fm = getattr(self, '_active_face_map', None)

        for layer_moves in step.free_layers:
            rotated_layer_moves = (
                [remap_moves(m, fm) if m else m for m in layer_moves]
                if fm else layer_moves
            )
            for m1 in rotated_layer_moves:
                for m2 in rotated_layer_moves:
                    for alg in cached_algs:
                        rotated_alg = remap_moves(alg, fm) if fm else alg
                        parts = [p for p in [m1, rotated_alg, m2] if p]
                        candidate = " ".join(parts)
                        candidate_state = self._join_moves(
                            self._join_moves(scramble, accumulated_solution), candidate
                        )
                        if self._check_already_solved(
                            step=step,
                            extra_directives=extra_directives,
                            accumulated_constraints=accumulated_constraints,
                            current_state=candidate_state,
                        ):
                            if DEBUG:
                                print(f"[CACHE HIT] '{step.name}': {candidate!r}")
                            return candidate
        return None

    # ── step execution ───────────────────────────────────────────────────────

    def _run_step(self, step, extra_directives, accumulated_constraints,
                  scramble, accumulated_solution):
        current_state = self._join_moves(scramble, accumulated_solution)

        # 1. Quick direct solve
        quick_out = None
        if ENABLE_QUICK_OUT:
            quick_out = self._run_solver(
                step=step, extra_directives=extra_directives,
                accumulated_constraints=accumulated_constraints,
                current_state=current_state, timeout=CACHE_TIMEOUT * QUICK_OUT_FACTOR,
            )
        if quick_out is not None:
            if not quick_out:
                if DEBUG: print(f"[QUICK SKIP] '{step.name}' already satisfied.")
                return ""
            if DEBUG: print(f"[QUICK SOLVE] '{step.name}': {quick_out[-1]!r}")
            return quick_out[-1]

        # 2. Cache lookup
        if step.cache_alg:
            hit = self._try_cache(
                step=step, extra_directives=extra_directives,
                accumulated_constraints=accumulated_constraints,
                scramble=scramble, accumulated_solution=accumulated_solution,
            )
            if hit is not None:
                return hit

        # 3. Full normal solve
        out_lines = self._run_solver(
            step=step, extra_directives=extra_directives,
            accumulated_constraints=accumulated_constraints,
            current_state=current_state, timeout=self.timeout,
        )
        if out_lines is None:
            return None
        if not out_lines:
            if DEBUG: print(f"[SKIP] '{step.name}' already satisfied.")
            return ""

        solution = out_lines[-1]
        if step.cache_alg and solution.strip():
            fm = getattr(self, '_active_face_map', None)
            canonical_solution = (
                remap_moves(solution, inverse_face_map(fm)) if fm else solution
            )
            existing = load_cache(self.workspace_root, self.method_name, step.name)
            if canonical_solution.strip() not in existing:
                append_cache(self.workspace_root, self.method_name, step.name, canonical_solution)
                if DEBUG:
                    print(f"[CACHE WRITE] '{step.name}': {canonical_solution!r}")

        return solution

    # ── helpers ──────────────────────────────────────────────────────────────

    @staticmethod
    def _join_moves(a, b):
        a, b = a.strip(), b.strip()
        if not a: return b
        if not b: return a
        return a + " " + b
