"""
predict py — Score a method given its feature vector.

Input:  method_vector(method) from generation.data_generation
Output: predicted score (float)

Not yet implemented.
"""

import os
import warnings
 
import joblib
import numpy as np
 
from ml.features import extract_from_method

# Model cache  (keyed by absolute path so multiple workspaces don't collide)
 
_MODEL_CACHE: dict = {}

def _model_path(workspace_root: str) -> str:
    return os.path.join(workspace_root, "data", "ml", "model.pkl")


# load model from disk
def load_model(workspace_root: str):

    path = os.path.abspath(_model_path(workspace_root))
 
    if path not in _MODEL_CACHE:
        if not os.path.exists(path):
            warnings.warn(
                f"[ml.predict] No model found at {path}. "
                "Run `python -m ml.train` first.",
                RuntimeWarning,
                stacklevel=2,
            )
            return None
        _MODEL_CACHE[path] = joblib.load(path)
 
    return _MODEL_CACHE[path]

# clear in process model cache
def invalidate_cache(workspace_root=None):
    if workspace_root is None:
        _MODEL_CACHE.clear()
    else:
        path = os.path.abspath(_model_path(workspace_root))
        _MODEL_CACHE.pop(path, None)
        

# Hypothesis (matches train.py exactly)
 
# apply the learned hypothesis to a single feature vector
def _predict_from_model(model: dict, x_raw: np.ndarray) -> float:

    theta = model["theta"]   # shape (n+1,)
    mean  = model["mean"]    # shape (n,)
    std   = model["std"]     # shape (n,)
 
    x_norm = (x_raw - mean) / std          # normalize with training stats
    x_b    = np.concatenate([[1.0], x_norm])  # prepend bias term
    return float(np.dot(theta, x_b))

# predict score without running solves
def predict(method, workspace_root: str):

    model = load_model(workspace_root)
    if model is None:
        return None
 
    x_raw = extract_from_method(method)
    return _predict_from_model(model, x_raw)