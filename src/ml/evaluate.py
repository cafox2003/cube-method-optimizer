"""
evaluate.py - Compare predicted vs actual scores from methods.csv
Usage: python -m ml.evaluate [workspace]
"""
import sys
import csv
import os
import numpy as np
from core.config import CONFIG
from ml.predict import load_model, _predict_from_model
from ml.features import FEATURE_COLS, extract_from_row

def main():
    default_ws = CONFIG["general"]["default_workspace"]
    workspace  = sys.argv[1] if len(sys.argv) > 1 else default_ws

    model = load_model(workspace)
    if model is None:
        print("No model found. Run python -m ml.train first.")
        return

    path = os.path.join(workspace, "data", "methods", "methods.csv")

    results = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            name = row.get("method_name", "").strip()
            score_str = row.get("score", "").strip()
            if not score_str:
                continue
            actual = float(score_str)
            x_raw = extract_from_row(row)
            predicted = _predict_from_model(model, x_raw)
            results.append((name, actual, predicted))

    results.sort(key=lambda r: r[1])

    print(f"\n{'Method':<40} {'Actual':>10} {'Predicted':>10} {'Error':>10} {'Error %':>10}")
    
    for name, actual, predicted in results:
        error = predicted - actual
        error_pct = (error / actual) * 100 if actual != 0 else float("nan")
        print(f"{name:<40} {actual:>10.6f} {predicted:>10.6f} {error:>+10.6f} {error_pct:>+9.2f}%")

    errors = [r[2] - r[1] for r in results]
    if errors:
        mae = np.mean(np.abs(errors))
        abs_pct_errors = [
            abs((predicted - actual) / actual) * 100
            for _, actual, predicted in results
            if actual != 0
        ]
        print(f"\n  Mean absolute error: {mae:.6f}")
        if abs_pct_errors:
            print(f"  Mean absolute percentage error: {np.mean(abs_pct_errors):.2f}%")
        print(f"  Max over-prediction:       {max(errors):+.6f}")
        print(f"  Max under-prediction:      {min(errors):+.6f}")

if __name__ == "__main__":
    main()
