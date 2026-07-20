"""
Application-wide constants.

This module centralizes fixed values used throughout the application
to avoid magic strings and duplicated literals.
"""

# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------

APP_AUTHOR = "Mohammed Faiyaz"
APP_DESCRIPTION = "Autonomous AI Document Generation Agent"

# ------------------------------------------------------------------
# API
# ------------------------------------------------------------------

API_PREFIX = "/api"
API_VERSION = "/v1"

HEALTH_ENDPOINT = "/health"
AGENT_ENDPOINT = "/agent"

# ------------------------------------------------------------------
# Document Types
# ------------------------------------------------------------------

REPORT = "report"
ESSAY = "essay"
SUMMARY = "summary"
LETTER = "letter"
MEETING_NOTES = "meeting_notes"

SUPPORTED_DOCUMENT_TYPES = (
    REPORT,
    ESSAY,
    SUMMARY,
    LETTER,
    MEETING_NOTES,
)

# ------------------------------------------------------------------
# Agent Status
# ------------------------------------------------------------------

STATUS_PENDING = "pending"
STATUS_PLANNING = "planning"
STATUS_EXECUTING = "executing"
STATUS_REFLECTING = "reflecting"
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"

# ------------------------------------------------------------------
# File Extensions
# ------------------------------------------------------------------

DOCX_EXTENSION = ".docx"
TEXT_EXTENSION = ".txt"
JSON_EXTENSION = ".json"

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------

DEFAULT_LOGGER_NAME = "autonomous_agent"

# ------------------------------------------------------------------
# Defaults
# ------------------------------------------------------------------

MAX_PLAN_STEPS = 10
DEFAULT_TIMEOUT_SECONDS = 60
MAX_DOCUMENT_TITLE_LENGTH = 120
