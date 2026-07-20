"""
Main entry point for the Autonomous Document Agent.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers.agent import router as agent_router
from app.api.routers.documents import router as documents_router
from app.api.routers.health import router as health_router
from app.core.config import settings
from app.core.lifecycle import (
    initialize_application,
    shutdown_application,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """
    initialize_application()
    yield
    shutdown_application()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
    "Autonomous AI Document Generation Agent "
    "built with FastAPI and Groq."
    ),
    lifespan=lifespan,
)

# Register API Routers
app.include_router(health_router)
app.include_router(agent_router)
app.include_router(documents_router)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """
    Root endpoint.
    """
    return {
        "message": (
            f"Welcome to {settings.app_name}"
        ),
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health",
    }