from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mangabible.app.constants import APP_INFO


@dataclass
class Project:
    """In-memory representation of a Manga Bible project.
    This model is completely independent of Qt/PySide6 to allow
    isolated unit testing.
    """

    name: str
    root_path: Path
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    app_version: str = APP_INFO.version
    project_format_version: int = 1

    @property
    def manifest_path(self) -> Path:
        """Returns the full file path to the .mbproj manifest file."""
        return self.root_path / f"{self.name}.mbproj"

    def to_dict(self) -> dict[str, Any]:
        """Serializes project attributes into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "root_path": str(self.root_path),
            "created_at": self.created_at.isoformat(),
            "app_version": self.app_version,
            "project_format_version": self.project_format_version,
        }
