# Developer Journal

## July 19, 2026
**Current Phase:** Project Setup

### What I did today:
- Set up the GitHub repo and cloned it locally.
- Created the core project folders.
- Built a Python virtual environment (`.venv`).
- Installed the base dev tools: PySide6, pytest, ruff, black, and mypy.
- Designed and initialized the clean `README.md` and permissive `LICENSE` (MIT).
- Configured a precise project `.gitignore` file.
- Initialized all structural sub-packages with `__init__.py` markers under `src/mangabible/`.
- Created the foundational `CHANGELOG.md` file.

### Decisions:
- **`src/` layout strategy:** We chose a `src/` layout to prevent accidental imports from the project root and ensure it matches common Python packaging practices.
- **MIT License choice:** Selected the MIT license to keep foundational development simple and open, leaving room to change it if commercial goals emerge later.

### Issues faced:
- Terminal theme hid the `(.venv)` prompt prefix, but verified activation via environment paths. No blocker.

### Plan for next session:
- Set up and configure the `pyproject.toml` file.

## July 20, 2026
**Current Phase:** Application Framework & UI Restructuring

### What I did today:
- Updated `application.py` to set Qt application metadata (`APP_INFO.name`, `version`, `organization`).
- Separated UI components into dedicated `ui/views/` and `ui/controllers/` packages.
- Added strict `pyproject.toml` project root discovery error handling in `paths.py`.
- Formatted and validated entire codebase against `black`, `ruff`, and `mypy` zero-error standards.

### Issues faced:
- Resolved `Activate.ps1` parser error by clearing post-signature additions.
- Resolved `APP_INFO` import name references and line length warnings in docstrings.

### Plan for next session:
- Implement `ProjectHubView`, `ProjectHubController`, and `ProjectService`.