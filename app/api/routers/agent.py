"""
Agent API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException

from app.agent.orchestrator import AgentOrchestrator
from app.schemas.api import AgentRequest, AgentResponse

router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)


def get_agent() -> AgentOrchestrator:
    """
    Dependency that provides an AgentOrchestrator instance.
    """
    return AgentOrchestrator()


@router.post("/run", response_model=AgentResponse)
def run_agent(
    request: AgentRequest,
    agent: AgentOrchestrator = Depends(get_agent),
) -> AgentResponse:
    """
    Execute the autonomous AI agent.
    """

    state = agent.run(request.user_request)

    if state.status == "failed":
        raise HTTPException(
            status_code=500,
            detail=state.errors,
        )

    return AgentResponse(
        status=state.status,
        generated_content=state.generated_content,
        reflection=state.reflection,
        errors=state.errors,
    )