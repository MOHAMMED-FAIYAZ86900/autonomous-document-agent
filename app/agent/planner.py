"""
Planner component for the Autonomous Document Agent.
"""

from app.agent.state import AgentState
from app.core.logging import get_logger
from app.llm.service import LLMService


class Planner:
    """
    Responsible for creating an execution plan
    from a user's natural language request.
    """

    def __init__(
        self,
        llm_service: LLMService | None = None,
    ) -> None:
        self.logger = get_logger(__name__)
        self.llm = llm_service or LLMService()

    def plan(
        self,
        state: AgentState,
    ) -> AgentState:
        """
        Generate an execution plan and update the agent state.
        """

        self.logger.info("Planning started.")

        state.status = "planning"

        try:
            response = self.llm.generate_plan(
                state.user_request
            )

            state.execution_plan = response.content

            state.status = "planned"

            self.logger.info("Planning completed.")

            return state

        except Exception as exc:

            self.logger.exception(
                "Planning failed."
            )

            state.status = "failed"

            state.errors.append(
                str(exc)
            )

            return state