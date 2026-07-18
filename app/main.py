"""
Main entry point for the Autonomous AI Agent.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers.health import router as health_router
from app.core.config import settings
from app.core.lifecycle import (
    initialize_application,
    shutdown_application,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application startup and shutdown.
    """
    initialize_application()
    yield
    shutdown_application()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Autonomous AI Document Generation Agent",
    lifespan=lifespan,
)

app.include_router(health_router)