from pathlib import Path

from mangabible.models.project import Project
from mangabible.repositories.project_repository import ProjectRepository


def test_repository_saves_project_and_creates_structure(tmp_path: Path) -> None:
    project_dir = tmp_path / "DemoManga"
    project = Project(name="DemoManga", root_path=project_dir)

    manifest_path = ProjectRepository.save(project)

    assert manifest_path.exists()
    assert (project_dir / "assets").is_dir()
    assert (project_dir / "scenes").is_dir()
    assert ProjectRepository.exists(project_dir)


def test_repository_exists_returns_false_for_missing_dir(tmp_path: Path) -> None:
    non_existent = tmp_path / "GhostProject"
    assert not ProjectRepository.exists(non_existent)
