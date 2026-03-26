"""
train py — Train a model to predict method score from method_vector features.

Input:  data/methods/methods.csv joined with data/evaluation/*.csv
Output: trained model artifact

Not yet implemented.
"""

import os
import sys
import csv
import joblib
import numpy as np
 
from ml.features import FEATURE_COLS, extract_from_row
from core.config import CONFIG
 
# Hyperparameters
 
LEARNING_RATE  = 0.01
NUM_ITERATIONS = 1000

def _methods_csv_path(workspace_root: str) -> str:
    return os.path.join(workspace_root, "data", "methods", "methods.csv")
 
def _model_path(workspace_root: str) -> str:
    return os.path.join(workspace_root, "data", "ml", "model.pkl")

# scan the data and return a score dict from most recent evaluation file
# fallback when methods.csv doesnt have scores yet
def _load_eval_scores(workspace_root: str) -> dict:

    eval_dir = os.path.join(workspace_root, "data", "evaluation")
    if not os.path.isdir(eval_dir):
        return {}
 
    eval_files = sorted(
        [f for f in os.listdir(eval_dir) if f.endswith(".csv")],
        reverse=True,
    )
 
    scores = {}
    for fname in eval_files:
        path = os.path.join(eval_dir, fname)
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            if "score" not in (reader.fieldnames or []):
                continue
            for row in reader:
                name      = row.get("method", "").strip()
                score_str = row.get("score", "").strip()
                if name and score_str and name not in scores:
                    try:
                        scores[name] = float(score_str)
                    except ValueError:
                        pass
 
    if scores:
        print(f"[INFO] Loaded {len(scores)} score(s) from evaluation CSV fallback.")
    return scores
 
# read methods.csv and return (X,y,method_names)
def load_training_data(workspace_root: str) -> tuple:

    path = _methods_csv_path(workspace_root)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"methods.csv not found at {path}. "
            "Run data_generation first to populate it."
        )
 
    eval_scores = None  # lazy-loaded only if needed
    X_rows, y_vals, names = [], [], []
    skipped = 0
 
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            method_name = row.get("method_name", "").strip()
            score_str   = row.get("score", "").strip()
            score       = None
 
            if score_str:
                try:
                    score = float(score_str)
                except ValueError:
                    pass
 
            if score is None:
                if eval_scores is None:
                    eval_scores = _load_eval_scores(workspace_root)
                score = eval_scores.get(method_name)
 
            if score is None:
                skipped += 1
                continue
 
            X_rows.append(extract_from_row(row))
            y_vals.append(score)
            names.append(method_name)
 
    if skipped:
        print(f"[INFO] Skipped {skipped} row(s) with no score.")
 
    if not X_rows:
        raise ValueError(
            "No scored rows found in methods.csv or evaluation CSVs.\n"
            "Run evaluate_solves() first, then retry training."
        )
 
    return np.array(X_rows), np.array(y_vals), names

# Normalization
 
# standardize features to zero mean and variance
def normalize(X: np.ndarray) -> tuple:

    mean          = X.mean(axis=0)
    std           = X.std(axis=0)
    # avoid division by zero for constant features
    std[std == 0] = 1   
    return (X - mean) / std, mean, std

# Hypothesis

# compute prediction for all m examples
def hypothesis(X_b: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return X_b @ theta

# Cost function

# MSE cost function from slides
def compute_cost(X_b: np.ndarray, y: np.ndarray, theta: np.ndarray) -> float:
    m      = len(y)
    errors = hypothesis(X_b, theta) - y
    return float((1 / (2 * m)) * np.dot(errors, errors))


# Gradient descent
 
# gradient descent for linear regression
def gradient_descent(
    X_b: np.ndarray,
    y: np.ndarray,
    alpha: float = LEARNING_RATE,
    num_iterations: int = NUM_ITERATIONS,
) -> tuple:

    m            = len(y)
    theta        = np.zeros(X_b.shape[1])   # initialise all θ to 0
    cost_history = []
 
    for i in range(num_iterations):
        errors = hypothesis(X_b, theta) - y     # (hθ(xᵢ) - yᵢ) for all i
        grad   = (1 / m) * (X_b.T @ errors)     # vectorised update across all θⱼ
        theta  = theta - alpha * grad            # simultaneous update
 
        if i % 100 == 0 or i == num_iterations - 1:
            cost = compute_cost(X_b, y, theta)
            cost_history.append(cost)
            print(f"  iter {i:>5d}   J(θ) = {cost:.8f}")
 
    return theta, cost_history


# Public API
 
def train(workspace_root: str) -> dict:

    print(f"[1/4] Loading training data from {_methods_csv_path(workspace_root)} ...")
    X, y, names = load_training_data(workspace_root)
    m, n = X.shape
    print(f"      {m} scored methods, {n} features.")
 
    print("[2/4] Normalizing features ...")
    X_norm, mean, std = normalize(X)
 
    # Prepend bias column of 1s so θ₀ acts as the intercept
    X_b = np.hstack([np.ones((m, 1)), X_norm])     # shape (m, n+1)
    print(f"      Feature matrix shape: {X_b.shape}  (includes bias column)")
 
    print(f"[3/4] Running gradient descent  (α={LEARNING_RATE}, {NUM_ITERATIONS} iters) ...")
    theta, cost_history = gradient_descent(X_b, y, alpha=LEARNING_RATE, num_iterations=NUM_ITERATIONS)
 
    # RMSE: cost is (1/2m)Σe², so e_rms = sqrt(2 * J_final)
    train_rmse = float(np.sqrt(2 * cost_history[-1]))
    print(f"      Final train RMSE: {train_rmse:.6f}")
 
    model = {"theta": theta, "mean": mean, "std": std}
 
    print("[4/4] Saving model ...")
    model_path = _model_path(workspace_root)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"      Saved to {model_path}")
    print(f"\n  Learned parameters:")
    print(f"      θ₀  {'(bias)':<35s} = {theta[0]:.6f}")
    for i, (col, w) in enumerate(zip(FEATURE_COLS, theta[1:]), 1):
        print(f"      θ{i:<2d}  {col:<35s} = {w:.6f}")
 
    return model

def main():
    default_ws = CONFIG["general"]["default_workspace"]
    workspace  = sys.argv[1] if len(sys.argv) > 1 else default_ws
    train(workspace)
 
 
if __name__ == "__main__":
    main()