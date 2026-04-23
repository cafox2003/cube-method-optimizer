"""
train py — Train a model to predict method score from method_vector features.

Input:  data/methods/methods.csv joined with data/evaluation/*.csv
Output: trained model artifact
"""

import os
import sys
import csv
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
 
from ml.features import FEATURE_COLS, extract_from_row
from core.config import CONFIG
 
# Hyperparameters
RANDOM_STATE = 42
N_ESTIMATORS = 200

# paths to methods csv and model file
def _methods_csv_path(workspace_root: str) -> str:
    return os.path.join(workspace_root, "data", "methods", "methods.csv")
 
def _model_path(workspace_root: str) -> str:
    return os.path.join(workspace_root, "data", "ml", "model.pkl")

# scan the data and return a score dict from most recent evaluation file
# fallback when methods.csv doesnt have scores yet
def _load_eval_scores(workspace_root: str) -> dict:
    # sets path to evaluation directory
    eval_dir = os.path.join(workspace_root, "data", "evaluation")
    if not os.path.isdir(eval_dir):
        return {}
    # lists all csv files in evaluation folder
    eval_files = sorted(
        [f for f in os.listdir(eval_dir) if f.endswith(".csv")],
        reverse=True,
    )
    # goes through each csv, opens it, and skips file without a score column
    scores = {}
    for fname in eval_files:
        path = os.path.join(eval_dir, fname)
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            if "score" not in (reader.fieldnames or []):
                continue
            # reads each row, gets method name and score
            # stores in scores dict, only keeps the first and latest score for each method
            for row in reader:
                name = row.get("method", "").strip()
                score_str = row.get("score", "").strip()
                if name and score_str and name not in scores:
                    try:
                        scores[name] = float(score_str)
                    except ValueError:
                        pass
    # prints how many scores were loaded
    if scores:
        print(f"Loaded {len(scores)} score(s) from evaluation CSV fallback.")
    return scores
 
# read methods.csv and return (X,y,method_names)
def load_training_data(workspace_root: str) -> tuple:
    # checks that methods.csv exists and raises error if not
    path = _methods_csv_path(workspace_root)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"methods.csv not found at {path}. "
            "Run data_generation first to populate it."
        )
 
    # cerates containers for features, labels, and method names
    eval_scores = None
    X_rows, y_vals, names = [], [], []
    # counts rows without scores
    skipped = 0
    
    # reads methods.csv row by row
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            method_name = row.get("method_name", "").strip()
            score_str   = row.get("score", "").strip()
            score       = None
            # converts score to float if its there
            if score_str:
                try:
                    score = float(score_str)
                except ValueError:
                    pass
            # if no score, fallback to evaluation csv scores
            if score is None:
                if eval_scores is None:
                    eval_scores = _load_eval_scores(workspace_root)
                score = eval_scores.get(method_name)
            # if still nothing, skip
            if score is None:
                skipped += 1
                continue
            # adds features
            X_rows.append(extract_from_row(row))
            # adds labels
            y_vals.append(score)
            # adds method names
            names.append(method_name)
    # prints out if there was anything skipped
    if skipped:
        print(f"Skipped {skipped} rows with no score.")
    # error if theres no data
    if not X_rows:
        raise ValueError(
            "No scored rows found in methods.csv or evaluation CSVs. Run evaluate_solves() first, then retry"
        )
    # converts features and labels to numpy arrays
    return np.array(X_rows), np.array(y_vals), names

# Public API
 
def train(workspace_root: str) -> dict:

    # load data
    print(f"Loading training data from {_methods_csv_path(workspace_root)} ...")
    X, y, names = load_training_data(workspace_root)
    m, n = X.shape
    print(f"      {m} scored methods, {n} features.")

    print(f"Training random forest regressor ({N_ESTIMATORS} trees)")
    estimator = RandomForestRegressor(
        n_estimators=N_ESTIMATORS,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    estimator.fit(X, y)

    predictions = estimator.predict(X)
    train_rmse = float(np.sqrt(np.mean((predictions - y) ** 2)))
    print(f"      Final train RMSE: {train_rmse:.6f}")

    # Keep the artifact shape dict-based so the rest of the API can stay stable.
    model = {
        "model_type": "random_forest",
        "estimator": estimator,
        "feature_cols": FEATURE_COLS,
    }
 
    print("Saving model")
    model_path = _model_path(workspace_root)
    # creates directories if missing, save to disk
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"      Saved to {model_path}")
    print("\n  Feature importances:")
    for col, importance in sorted(
        zip(FEATURE_COLS, estimator.feature_importances_),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"      {col:<35s} = {importance:.6f}")
 
    return model

def main():
    default_ws = CONFIG["general"]["default_workspace"]
    workspace  = sys.argv[1] if len(sys.argv) > 1 else default_ws
    train(workspace)
 
 
if __name__ == "__main__":
    main()
