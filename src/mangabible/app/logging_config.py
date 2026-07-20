import logging
import sys

from mangabible.app.paths import get_log_directory


def setup_logging() -> logging.Logger:
    logger = logging.getLogger("MangaBible")

    # GUARD: If logging handlers are already configured, do not add them again
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
    )

    # Console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File storage output
    log_file = get_log_directory() / "app.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logging()
