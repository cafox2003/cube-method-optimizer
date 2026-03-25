"""
search.py — Orchestrates the method discovery loop.

Loop:
    1. mutate.py generates candidate methods → workspace/scratch/dsl/
    2. generation.data_generation runs solves → workspace/scratch/data/
    3. ml.predict scores each candidate
    4. Promising methods are promoted to workspace/stable/

Scratch workspace can be cleared between runs without data loss.

Not yet implemented.
"""
