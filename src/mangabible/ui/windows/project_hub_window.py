from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout

from mangabible.app.constants import WINDOW_DEFAULTS
from mangabible.ui.windows.base_window import BaseWindow


class ProjectHubWindow(BaseWindow):
    """Initial hub window for creating / opening projects"""

    def __init__(self) -> None:
        super().__init__(title_suffix="Project Hub")
        self.resize(WINDOW_DEFAULTS.width, WINDOW_DEFAULTS.height)

        layout = QVBoxLayout()
        label = QLabel(" Welcome to Manga Bible")

        btn_create = QPushButton("Create New project")
        btn_open = QPushButton("Open Existing project")
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(btn_create)
        layout.addWidget(btn_open)
        layout.addWidget(btn_exit)

        self.setLayout(layout)
