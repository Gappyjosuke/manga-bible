# manga-bible

A desktop application designed to manage manga production workflows from a single workspace.

## Purpose
The project provides a structured environment for manga creation. Instead of using separate tools for script management, asset organization, storyboard tracking, and exporting, this application combines these tasks into one desktop interface.

## Planned Features
| Feature | Description |
| :--- | :--- |
| **Asset Directory** | A centralized system to organize character sheets, backgrounds, and reference images. |
| **Pipeline Automation** | Automated tasks for resizing, renaming, and backing up pages based on publishing standards. |
| **Quality Control** | Automated validation checks for manuscript metadata and file structures. |
| **Native Desktop UI** | A fast, responsive desktop interface built with PySide6. |

## Development Setup

### System Requirements
* Python 3.14 or newer
* Git

### Installation Steps
1. Clone the repository:
```bash
git clone [https://github.com/Gappyjosuke/manga-bible.git](https://github.com/Gappyjosuke/manga-bible.git)
cd manga-bible
```

2. Activate the virtual environment:
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate
  ```
* **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

3. Install development tools:
```bash
python -m pip install PySide6 pytest ruff black mypy
```

> **Important Note:** Always ensure your virtual environment is activated before installing packages or running development tools to avoid dependency conflicts.

## Project Roadmap
* **Phase 1:** Core system configuration and linter setup (`pyproject.toml`).
* **Phase 2:** Base UI layout design using PySide6.
* **Phase 3:** File tracking and asset management backend.
* **Phase 4:** Export functionality and test suite implementation.

## Contributing
This project is currently in early development. Detailed guidelines for code formatting, testing requirements, and contribution processes will be added as the framework updates.

## License
MIT License