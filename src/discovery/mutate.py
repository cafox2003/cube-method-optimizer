import copy
import random
import hashlib
import os
import sys
from typing import Optional

from core.models import Step, Group, Method
from core.dsl import method_to_file, method_to_dsl_text
from core.config import CONFIG

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MAX_CONSTRAINTS_PER_STEP = CONFIG["generation"]["max_constraints_per_step"]
TARGET_COUNT = CONFIG["generation"]["target_count"]

_ALL_EDGES = ["BL", "BR", "BU", "BD", "FL", "FR", "FU", "FD", "LU", "LD", "RU", "RD"]
_ALL_CORNERS = ["BLU", "BLD", "BRU", "BRD", "FLU", "FLD", "FRU", "FRD"]
_PIECE_POOL = _ALL_EDGES + _ALL_CORNERS # Exactly 20 pieces

def _piece_line(piece: str) -> str:
    if len(piece) == 2:
        return f"add_edge {piece}"
    return f"add_corner {piece}"

def safe_method_to_dsl(method: Method) -> str:
    """Safely converts Method to DSL, handling potential int-symmetry issues."""
    orig_sym = method.symmetry_orientations
    if method.symmetry_orientations:
        method.symmetry_orientations = [str(s) for s in method.symmetry_orientations]
    try:
        text = method_to_dsl_text(method)
    finally:
        method.symmetry_orientations = orig_sym
    return text

# ---------------------------------------------------------------------------
# Random Method Generator
# ---------------------------------------------------------------------------

def generate_random_method(name: str) -> Method:
    """
    Creates a valid 20-piece method with no wildcards.
    Distributes 20 pieces into 5 steps (4 pieces each) to stay under MAX.
    """
    method = Method(name=name, rotation_str="x2")
    
    # Shuffle the master pool
    pieces = list(_PIECE_POOL)
    random.shuffle(pieces)
    
    # Divide into 5 steps (20 / 4 = 5 steps)
    # This ensures we never hit the MAX_CONSTRAINTS_PER_STEP (5)
    step_size = 4
    for i in range(0, len(pieces), step_size):
        chunk = pieces[i : i + step_size]
        step_name = f"step_{i//step_size}"
        new_step = Step(name=step_name)
        new_step.constraints = [_piece_line(p) for p in chunk]
        method.items.append(new_step)
        
    return method

# ---------------------------------------------------------------------------
# Execution Block
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    default_ws = CONFIG["general"]["scratch_workspace"]
    workspace  = sys.argv[1] if len(sys.argv) > 1 else default_ws

    dsl_dir = os.path.join(workspace, "dsl")
    os.makedirs(dsl_dir, exist_ok=True)

    print(f"[1/2] Generating {TARGET_COUNT} random methods...")

    generated_count = 0
    seen_hashes = set()

    while generated_count < TARGET_COUNT:
        # 1. Generate a candidate
        candidate_name = f"random_gen_{generated_count}"
        method = generate_random_method(candidate_name)
        
        # 2. Hash it to ensure uniqueness
        dsl_string = safe_method_to_dsl(method)
        m_hash = hashlib.md5(dsl_string.encode()).hexdigest()
        
        if m_hash not in seen_hashes:
            seen_hashes.add(m_hash)
            
            # 3. Save to file
            # We use the hash in the filename to prevent overwrites
            method.name = f"rand_{m_hash[:8]}"
            method_to_file(method, workspace)
            
            generated_count += 1
            
            if generated_count % 100 == 0:
                print(f"  -> Generated {generated_count}/{TARGET_COUNT}")

    print(f"[2/2] Done! Saved {generated_count} unique random methods to {dsl_dir}")
