from mangabible.app.logging_config import logger
from mangabible.app.paths import find_project_root


def initialize_application() -> None:
    """Handles all non-UI initialization and system validation tasks
    before the app boots.
    """
    logger.info("Initializing system log configuration...")
    # Validate paths system
    root = find_project_root()
    logger.info(f"Project root directory resolved to: {root}")
    logger.info("Application bootstrap complete.")
