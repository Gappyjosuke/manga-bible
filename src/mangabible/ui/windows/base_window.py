from PySide6.QtWidgets import QWidget

from mangabible.app.constants import APP_INFO


class BaseWindow(QWidget):
    """Base class for all top-level window frames in Manga Bible"""

    def __init__(self, title_suffix: str = "") -> None:
        super().__init__()

        full_title = f"{APP_INFO.name}{APP_INFO.version}"
        if title_suffix:
            full_title += f" - {title_suffix}"

        self.setWindowTitle(full_title)
