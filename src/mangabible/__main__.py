from mangabible.app.application import run_application
from mangabible.app.bootstrap import initialize_application
from mangabible.app.logging_config import logger

if __name__ == "__main__":
    # 1. Run initialization chores first
    initialize_application()

    # 2. Launch the visual UI environment
    logger.info("Launching Project Hub visual interface...")
    run_application()
