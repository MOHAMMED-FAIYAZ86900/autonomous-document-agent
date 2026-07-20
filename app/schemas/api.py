"""
API request and response schemas.
"""

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """
    Incoming agent request.
    """

    user_request: str = Field(..., description="Natural language request.")


class AgentResponse(BaseModel):
    """
    Agent execution response.
    """

    status: str
    generated_content: str | None
    reflection: str | None
    errors: list[str]


class DocumentInfo(BaseModel):
    """
    Metadata describing a stored document.
    """

    filename: str
    size: int
