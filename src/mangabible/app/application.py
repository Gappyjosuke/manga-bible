import sys

from PySide6.QtWidgets import QApplication

from mangabible.app.constants import APP_INFO
from mangabible.ui.windows.project_hub_window import ProjectHubWindow


def run_application() -> None:
    """Initialized the Qt event loop and display the initial window"""
    app = QApplication(sys.argv)

    # configure Qt internal application metadata
    app.setApplicationName(APP_INFO.name)
    app.setApplicationVersion(APP_INFO.version)
    app.setOrganizationName(APP_INFO.organization)

    hub = ProjectHubWindow()
    hub.show()
    sys.exit(app.exec())
