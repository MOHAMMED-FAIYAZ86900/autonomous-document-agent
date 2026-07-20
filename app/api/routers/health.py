"""
Health check endpoints.
"""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    """
    Return application health information.
    """

    return {
        "status": "healthy",
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }
