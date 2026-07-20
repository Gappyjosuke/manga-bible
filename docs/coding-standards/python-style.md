# Python Coding Standards - Manga Bible

## Code Quality Foundations
* **Strict Formatting:** All modules must conform to standards enforced by `black` and `ruff` configurations.
* **Types Definition:** All functions and parameters require clear static type annotations to guarantee compilation safety using `mypy`.
* **Zero Logging Prints:** Raw `print()` commands are forbidden. Always import the engine logger framework via `from mangabible.app.logging_config import logger`.