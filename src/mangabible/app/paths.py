import os
from pathlib import Path


def find_project_root() -> Path:
    """Climbs up from the current file path to dynamically
    find the project root folder"""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    # Fallback to the current working directory if not found
    raise RuntimeError(
        "Could not locate project root. Expected to find pyproject.toml."
    )


ROOT_DIR = find_project_root()


def get_log_directory() -> Path:
    log_dir = ROOT_DIR / "logs"
    os.makedirs(log_dir, exist_ok=True)
    return log_dir
