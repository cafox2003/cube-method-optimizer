from dataclasses import dataclass


# ---------------------------------------------------------------------------
# DSL data model
# ---------------------------------------------------------------------------

class Step:
    def __init__(self, name, cache_alg=False, free_layers=None):
        self.name = name
        self.constraints = []
        self.cache_alg = cache_alg
        self.free_layers = free_layers or []


class Group:
    _BASE_ORDERS = {"in_order", "random", "best", "worst"}

    def __init__(self, name, order="in_order"):
        self.name = name
        self.order = order
        self.directives = []
        self.steps = []


class Remove:
    def __init__(self, command):
        self.command = command


class Method:
    def __init__(self, name, rotation_str="", symmetry_orientations=None, symmetry_depth=1):
        self.name = name
        self.items = []
        # Fixed beforehand rotation (e.g. "x2"). Applied to scramble before every
        # solver call; solutions come back in the rotated frame.
        self.rotation_str: str = rotation_str.strip()
        # Symmetry selection: list of orientation indices to try.
        self.symmetry_orientations: list = symmetry_orientations or []
        # How many top-level items to evaluate per orientation candidate.
        self.symmetry_depth: int = symmetry_depth


# ---------------------------------------------------------------------------
# Solve result
# ---------------------------------------------------------------------------

@dataclass
class StepResult:
    name: str
    solution: str  # moves string, "" if step was already satisfied


@dataclass
class SolveResult:
    scramble: str           # original scramble (pre-rotation)
    orientation: str        # rotation string applied, e.g. "x2 y", or "" if none
    steps: list             # list[StepResult], in execution order
    failed: bool = False    # True if any step aborted mid-solve


def format_solve_result(result: SolveResult) -> str:
    """Reconstruct the human-readable solve output from a SolveResult."""
    lines = [f"{result.scramble} //scramble"]
    if result.orientation:
        lines.append(f"{result.orientation} //orientation")
    for step in result.steps:
        lines.append(f"{step.solution} //{step.name}")
    return "\n".join(lines)
