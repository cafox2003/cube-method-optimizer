import os


def cache_path(workspace_root: str, method_name: str, step_name: str) -> str:
    return os.path.join(workspace_root, "algs", method_name, f"{step_name}_algs.txt")


def load_cache(workspace_root: str, method_name: str, step_name: str) -> list:
    path = cache_path(workspace_root, method_name, step_name)
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def append_cache(workspace_root: str, method_name: str, step_name: str, alg: str):
    path = cache_path(workspace_root, method_name, step_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(alg.strip() + "\n")
