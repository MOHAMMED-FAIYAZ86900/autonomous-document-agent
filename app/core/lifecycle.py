"""
Application lifecycle management.

This module initializes and shuts down application resources.
"""

from pathlib import Path

from app.core.config import settings
from app.core.exceptions import ConfigurationError
from app.core.logging import configure_logging, get_logger


def initialize_application() -> None:
    """
    Initialize application resources during startup.
    """

    # Configure logging first
    configure_logging()

    logger = get_logger(__name__)

    logger.info("Initializing application...")

    # Validate required configuration
    if not settings.gemini_api_key:
        logger.warning(
        "GEMINI_API_KEY is not configured. "
        "LLM features will be unavailable."
    )

    

    # Ensure output directory exists
    Path(settings.output_dir).mkdir(
        parents=True,
        exist_ok=True,
    )

    logger.info("Output directory: %s", settings.output_dir)
    logger.info("Environment: %s", settings.environment)
    logger.info("Application initialized successfully.")


def shutdown_application() -> None:
    """
    Perform graceful application shutdown.
    """

    logger = get_logger(__name__)

    logger.info("Application shutdown complete.")