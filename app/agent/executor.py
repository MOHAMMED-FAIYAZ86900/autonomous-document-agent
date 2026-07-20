"""
Execution engine for the Autonomous Document Agent.
"""

from app.agent.state import AgentState
from app.core.logging import get_logger
from app.llm.service import LLMService


class Executor:
    """
    Executes the execution plan and generates
    the initial document.
    """

    def __init__(
        self,
        llm_service: LLMService | None = None,
    ) -> None:

        self.logger = get_logger(__name__)
        self.llm = llm_service or LLMService()

    def execute(
        self,
        state: AgentState,
    ) -> AgentState:
        """
        Execute the generated plan.
        """

        self.logger.info("AI content generation started.")

        state.status = "executing"

        try:

            response = self.llm.generate_document(
                state.execution_plan
            )

            state.generated_content = response.content

            state.status = "executed"

            self.logger.info(
                "AI content generated successfully."
            )

            return state

        except Exception as exc:

            self.logger.exception(
                "Execution failed."
            )

            state.status = "failed"

            state.errors.append(
                str(exc)
            )

            return state