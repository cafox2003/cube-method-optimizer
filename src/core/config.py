# src/core/config.py

import os
import tomllib
import psutil

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.toml")


def load_config():
    with open(CONFIG_PATH, "rb") as f:
        return tomllib.load(f)


CONFIG = load_config()


def compute_max_workers():
    cfg = CONFIG["parallel"]

    # Parallel disabled → single process
    if not cfg.get("enabled", True):
        return 1

    # Hard override
    if cfg.get("max_workers") is not None:
        return cfg["max_workers"]

    total_mem = psutil.virtual_memory().total

    memory_fraction = cfg.get("memory_fraction", 0.3)
    safety_buffer_gb = cfg.get("safety_buffer_gb", 8)
    per_worker_gb = cfg.get("memory_per_worker_gb", 6)

    usable_mem = total_mem * memory_fraction
    safety_buffer = safety_buffer_gb * (1024**3)
    per_worker = per_worker_gb * (1024**3)

    available = max(usable_mem - safety_buffer, per_worker)

    max_workers = int(available // per_worker)

    return max(1, max_workers)
