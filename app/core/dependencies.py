"""
Application dependency providers.

This module centralizes dependency creation for FastAPI.
"""

from app.core.config import settings
from app.core.logging import get_logger


def get_settings():
    """
    Return the application settings.
    """
    return settings


def get_app_logger():
    """
    Return the application logger.
    """
    return get_logger("autonomous_agent")