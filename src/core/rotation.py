"""
rotation.py — Cube orientation and move-remapping system for the method solver DSL.

Design
------
All 24 cube orientations are tracked via face-normal mapping derived from 3D rotation
matrices. Proper rotations (det=1) never flip move directions — CW stays CW.

The key operation this module provides:
    remap_moves(move_string, face_map) -> new_move_string

Example:
    remap_moves_by_rotation("R U R' U'", "x2")  ->  "R D R' D'"

This lets the pipeline remap a scramble into the solver's rotated frame, then present
the solution prefixed with the rotation token (e.g. "x2 R D R' D'") so the user
knows to hold the cube in that orientation.

Cubing conventions
------------------
- x: CW around the R face axis when viewed from outside → U→F, F→D, D→B, B→U
- y: CW around the U face axis when viewed from outside → F→R, R→B, B→L, L→F
- z: CW around the F face axis when viewed from outside → R→U, U→L, L→D, D→R
- No direction flips occur under any proper rotation (proven: det(R)=+1 ⟹ chirality preserved).
"""

from __future__ import annotations
import re
import numpy as np
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Face normals
# ---------------------------------------------------------------------------

_FACE_NORMALS: Dict[str, np.ndarray] = {
    'U': np.array([ 0,  1,  0]),
    'D': np.array([ 0, -1,  0]),
    'F': np.array([ 0,  0,  1]),
    'B': np.array([ 0,  0, -1]),
    'R': np.array([ 1,  0,  0]),
    'L': np.array([-1,  0,  0]),
}

def _normal_to_face(v: np.ndarray) -> str:
    for f, n in _FACE_NORMALS.items():
        if np.allclose(v, n):
            return f
    raise ValueError(f"No face matches normal {v}")


# ---------------------------------------------------------------------------
# Rotation matrices (CW from outside = CCW mathematical convention)
# ---------------------------------------------------------------------------

def _rot_mat(axis: str, quarter_turns: int = 1) -> np.ndarray:
    angle = quarter_turns * (np.pi / 2)
    c = int(round(np.cos(angle)))
    s = int(round(np.sin(angle)))
    if axis == 'x':
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    elif axis == 'y':
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    elif axis == 'z':
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    raise ValueError(f"Unknown axis '{axis}'")

def _face_map(mat: np.ndarray) -> Dict[str, str]:
    return {f: _normal_to_face(mat @ n) for f, n in _FACE_NORMALS.items()}

def _identity_face_map() -> Dict[str, str]:
    return {f: f for f in _FACE_NORMALS}

def _compose(m1: Dict[str, str], m2: Dict[str, str]) -> Dict[str, str]:
    return {f: m2[m1[f]] for f in m1}

def inverse_face_map(face_map: Dict[str, str]) -> Dict[str, str]:
    """Return the inverse of a face map (the reverse rotation)."""
    return {v: k for k, v in face_map.items()}

def _freeze(m: Dict[str, str]) -> tuple:
    return tuple(sorted(m.items()))


# Primitive face maps for all 9 rotation tokens
_PRIM_MAPS: Dict[str, Dict[str, str]] = {
    'x':  _face_map(_rot_mat('x', 1)),
    "x'": _face_map(_rot_mat('x', 3)),
    'x2': _face_map(_rot_mat('x', 2)),
    'y':  _face_map(_rot_mat('y', 1)),
    "y'": _face_map(_rot_mat('y', 3)),
    'y2': _face_map(_rot_mat('y', 2)),
    'z':  _face_map(_rot_mat('z', 1)),
    "z'": _face_map(_rot_mat('z', 3)),
    'z2': _face_map(_rot_mat('z', 2)),
}

assert _PRIM_MAPS['x']['U'] == 'F'
assert _PRIM_MAPS['x2']['U'] == 'D'
assert _PRIM_MAPS['x2']['F'] == 'B'
assert _PRIM_MAPS['y']['F'] == 'R'
assert _PRIM_MAPS['z']['R'] == 'U'


# ---------------------------------------------------------------------------
# Parse rotation string → face map
# ---------------------------------------------------------------------------

def parse_rotation(rotation_str: str) -> Dict[str, str]:
    """
    Parse a rotation string like "x2 y'" into a composed face→face map.
    Empty string → identity map.
    """
    result = _identity_face_map()
    for tok in rotation_str.strip().split():
        tok_lower = tok.lower()
        if tok_lower not in _PRIM_MAPS:
            raise ValueError(
                f"Unknown rotation token '{tok}'. "
                f"Valid: {sorted(_PRIM_MAPS)}"
            )
        result = _compose(result, _PRIM_MAPS[tok_lower])
    return result


# ---------------------------------------------------------------------------
# All 24 orientations
# ---------------------------------------------------------------------------

def _generate_all_24() -> List[Tuple[str, Dict[str, str]]]:
    """BFS over x, y, z generators to enumerate all 24 orientations."""
    identity = _identity_face_map()
    seen: Dict[tuple, Tuple[Dict, str]] = {_freeze(identity): (identity, "")}
    queue = [(identity, "")]
    while queue:
        cur_map, cur_path = queue.pop(0)
        for tok in ("x", "y", "z"):
            nxt = _compose(cur_map, _PRIM_MAPS[tok])
            key = _freeze(nxt)
            if key not in seen:
                path = (cur_path + " " + tok).strip()
                seen[key] = (nxt, path)
                queue.append((nxt, path))
    assert len(seen) == 24
    return [(path, m) for (m, path) in seen.values()]


_ALL_24: List[Tuple[str, Dict[str, str]]] = _generate_all_24()
_MAP_TO_IDX: Dict[tuple, int] = {_freeze(m): i for i, (_, m) in enumerate(_ALL_24)}

_IDENTITY_IDX: int = next(
    i for i, (_, m) in enumerate(_ALL_24) if m == _identity_face_map()
)


def orientation_rotation_string(idx: int) -> str:
    """Canonical rotation string for orientation index idx."""
    return _ALL_24[idx][0]

def orientation_face_map(idx: int) -> Dict[str, str]:
    """Face map for orientation index idx."""
    return _ALL_24[idx][1]

def identity_orientation_index() -> int:
    return _IDENTITY_IDX

def rotation_string_to_orientation_index(rot_str: str) -> int:
    """Parse a rotation string and return its orientation index."""
    face_map = parse_rotation(rot_str)
    key = _freeze(face_map)
    if key not in _MAP_TO_IDX:
        raise ValueError(f"'{rot_str}' does not map to a valid cube orientation")
    return _MAP_TO_IDX[key]


# ---------------------------------------------------------------------------
# Move remapping
# ---------------------------------------------------------------------------

_MOVE_RE = re.compile(r"^([UDFBRL])(w?)(2|')?$", re.IGNORECASE)
_ROT_RE  = re.compile(r"^[xyz][2']?$", re.IGNORECASE)


def remap_move_token(token: str, face_map: Dict[str, str]) -> str:
    """
    Remap a single move token through a face map.
    Rotation tokens (x, y', z2) pass through unchanged.
    No direction flips — proper rotations preserve chirality.
    """
    t = token.strip()
    if not t or _ROT_RE.match(t):
        return t
    m = _MOVE_RE.match(t)
    if not m:
        return t
    face   = m.group(1).upper()
    wide   = m.group(2)
    suffix = m.group(3) or ''
    return face_map.get(face, face) + wide + suffix


def remap_moves(move_string: str, face_map: Dict[str, str]) -> str:
    """Remap all move tokens in `move_string` through `face_map`."""
    if not move_string.strip():
        return move_string
    return " ".join(remap_move_token(t, face_map) for t in move_string.strip().split())


def remap_moves_by_rotation(move_string: str, rotation_str: str) -> str:
    """Convenience: remap moves by a rotation string like "x2" or "y z'"."""
    if not rotation_str.strip():
        return move_string
    return remap_moves(move_string, parse_rotation(rotation_str))


# ---------------------------------------------------------------------------
# Macros and symmetry parameter parsing
# ---------------------------------------------------------------------------

def _face_on_top(face: str) -> List[int]:
    return [i for i, (_, m) in enumerate(_ALL_24) if m['U'] == face]

_MACRO_DEFS: Dict[str, List[int]] = {
    "all":   list(range(24)),
    "fixed": [_IDENTITY_IDX],
    "U":     _face_on_top('U'),
    "F":     _face_on_top('F'),
    "R":     _face_on_top('R'),
    "B":     _face_on_top('B'),
    "L":     _face_on_top('L'),
    "D":     _face_on_top('D'),
}


def _tokenise_symmetry(s: str) -> List[str]:
    tokens, current = [], []
    in_quote, quote_char = False, None
    for ch in s:
        if ch in ('"', "'") and not in_quote:
            in_quote, quote_char = True, ch
            current.append(ch)
        elif ch == quote_char and in_quote:
            in_quote, quote_char = False, None
            current.append(ch)
        elif ch == ',' and not in_quote:
            tokens.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        tokens.append("".join(current).strip())
    return [t for t in tokens if t]


def expand_symmetry_param(param: str) -> List[int]:
    """
    Parse the symmetry= DSL value (e.g. 'U,F,"x2 y\\'",fixed').
    Returns a deduplicated sorted list of orientation indices.
    """
    indices: set = set()
    for tok in _tokenise_symmetry(param):
        tok = tok.strip().strip('"').strip("'")
        if tok in _MACRO_DEFS:
            indices.update(_MACRO_DEFS[tok])
        else:
            idx = rotation_string_to_orientation_index(tok)
            indices.add(idx)
    return sorted(indices)


# ---------------------------------------------------------------------------
# Constraint line remapping
# ---------------------------------------------------------------------------

_FACE_LETTERS = set('UDFBRL')

_NO_REMAP_KEYWORDS = {
    'add_edges_orientation',
    'add_corners_orientation',
    'add_corners_permutation',
    'add_edges_permutation',
    'max_length',
    'init_empty_cube',
    'solve',
}


def remap_constraint_line(line: str, face_map: Dict[str, str]) -> str:
    """Remap face letters in a solver constraint line through face_map."""
    tokens = line.strip().split()
    if not tokens:
        return line
    keyword = tokens[0]
    if keyword in _NO_REMAP_KEYWORDS or len(tokens) == 1:
        return line
    args = tokens[1:]

    def remap_tok(tok: str) -> str:
        return ''.join(
            face_map.get(ch, ch) if ch in _FACE_LETTERS else ch
            for ch in tok
        )

    return keyword + ' ' + ' '.join(remap_tok(a) for a in args)


def remap_constraint_lines(lines: list, face_map: Dict[str, str]) -> list:
    """Remap a list of constraint lines. Returns a new list."""
    return [remap_constraint_line(line, face_map) for line in lines]
