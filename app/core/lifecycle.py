"""
Application lifecycle management.
"""

from pathlib import Path

from app.core.config import settings
from app.core.logging import configure_logging, get_logger


def initialize_application() -> None:
    configure_logging()

    logger = get_logger(__name__)

    logger.info("Initializing application...")

    if settings.llm_provider == "groq":

        if not settings.groq_api_key:
            raise RuntimeError(
                "GROQ_API_KEY is not configured."
            )

    Path(settings.output_dir).mkdir(
        parents=True,
        exist_ok=True,
    )

    logger.info("Output directory: %s", settings.output_dir)
    logger.info("Environment: %s", settings.environment)
    logger.info("Application initialized successfully.")


def shutdown_application() -> None:

    logger = get_logger(__name__)

    logger.info("Application shutdown complete.")