from pathlib import Path

from mangabible.app.constants import APP_INFO
from mangabible.models.project import Project


def test_project_model_initialization(tmp_path: Path) -> None:
    project = Project(name="Test Manga", root_path=tmp_path)

    assert project.name == "Test Manga"
    assert project.root_path == tmp_path
    assert project.manifest_path == tmp_path / "Test Manga.mbproj"
    assert project.project_format_version == 1
    assert project.app_version == APP_INFO.version


def test_project_to_dict_serialization(tmp_path: Path) -> None:
    project = Project(name="Test Manga", root_path=tmp_path)
    data = project.to_dict()

    assert data["name"] == "Test Manga"
    assert data["app_version"] == APP_INFO.version
    assert "created_at" in data
