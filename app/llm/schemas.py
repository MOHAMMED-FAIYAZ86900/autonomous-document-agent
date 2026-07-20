"""
Pydantic models for LLM requests and responses.
"""

from pydantic import BaseModel, Field


class LLMRequest(BaseModel):
    """
    Represents a request sent to an LLM provider.
    """

    prompt: str = Field(
        ...,
        description="Prompt sent to the language model.",
    )

    system_prompt: str | None = Field(
        default=None,
        description="Optional system instruction.",
    )

    temperature: float = Field(
        default=0.3,
        ge=0.0,
        le=2.0,
        description="Sampling temperature.",
    )

    max_tokens: int = Field(
        default=2048,
        gt=0,
        description="Maximum number of output tokens.",
    )

    response_as_json: bool = Field(
        default=False,
        description="Whether structured JSON output is requested.",
    )


class LLMResponse(BaseModel):
    """
    Represents a response returned by an LLM provider.
    """

    content: str = Field(
        ...,
        description="Generated response text.",
    )

    model: str = Field(
        ...,
        description="Model used for generation.",
    )

    success: bool = Field(
        default=True,
        description="Whether the request completed successfully.",
    )

    finish_reason: str | None = Field(
        default=None,
        description="Reason generation stopped.",
    )