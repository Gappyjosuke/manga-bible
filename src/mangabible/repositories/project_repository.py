import json
from pathlib import Path
from typing import Any

from mangabible.models.project import Project


class ProjectRepository:
    """Handles disk persistence (read/write operations) for Project models."""

    @staticmethod
    def save(project: Project) -> Path:
        """Creates the project root directory, default folder scaffolding,
        and writes the .mbproj JSON manifest file.
        """
        # Create root project directory and scaffolding subdirectories
        project.root_path.mkdir(parents=True, exist_ok=True)
        (project.root_path / "assets").mkdir(exist_ok=True)
        (project.root_path / "scenes").mkdir(exist_ok=True)

        # Write project manifest JSON file
        manifest_data: dict[str, Any] = project.to_dict()
        manifest_file = project.manifest_path

        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=4)

        return manifest_file

    @staticmethod
    def exists(project_dir: Path) -> bool:
        """Checks if a valid project directory exists at the target path."""
        if not project_dir.is_dir():
            return False
        return any(project_dir.glob("*.mbproj"))
