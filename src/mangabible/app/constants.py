from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationInfo:
    name: str = "Manga Bible"
    version: str = "0.2.0"
    organization: str = "Manga Bible"
    project_extension: str = ".mbproj"


@dataclass(frozen=True)
class WindowDefaults:
    width: int = 600
    height: int = 400


APP_INFO = ApplicationInfo()
WINDOW_DEFAULTS = WindowDefaults()
