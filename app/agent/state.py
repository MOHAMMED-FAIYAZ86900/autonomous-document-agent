"""
Agent state model for the Autonomous Document Agent.
"""

from pydantic import BaseModel, Field


class AgentState(BaseModel):
    """
    Stores the complete execution state of the autonomous agent.
    """

    user_request: str = Field(
        ...,
        description="Original user request."
    )

    document_type: str | None = Field(
        default=None,
        description="Detected document type."
    )

    execution_plan: str | None = Field(
        default=None,
        description="Generated execution plan."
    )

    assumptions: list[str] = Field(
        default_factory=list,
        description="Planner assumptions."
    )

    generated_content: str | None = Field(
        default=None,
        description="Generated document."
    )

    reflection: str | None = Field(
        default=None,
        description="Reflection feedback."
    )

    output_file: str | None = Field(
        default=None,
        description="Generated DOCX path."
    )

    status: str = Field(
        default="pending",
        description="Current agent status."
    )

    errors: list[str] = Field(
        default_factory=list,
        description="Execution errors."
    )