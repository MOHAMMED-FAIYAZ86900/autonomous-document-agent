"""
Reflection engine for the Autonomous Document Agent.
"""

from app.agent.state import AgentState
from app.core.logging import get_logger
from app.llm.service import LLMService


class Reflector:
    """
    Reviews generated documents and provides
    improvement feedback.
    """

    def __init__(
        self,
        llm_service: LLMService | None = None,
    ) -> None:

        self.logger = get_logger(__name__)
        self.llm = llm_service or LLMService()

    def review(
        self,
        state: AgentState,
    ) -> AgentState:
        """
        Review the generated document.
        """

        self.logger.info(
            "Reflection started."
        )

        state.status = "reflecting"

        try:

            response = self.llm.review_document(
                state.generated_content
            )

            state.reflection = response.content

            state.status = "reviewed"

            self.logger.info(
                "Reflection completed."
            )

            return state

        except Exception as exc:

            self.logger.exception(
                "Reflection failed."
            )

            state.status = "failed"

            state.errors.append(
                str(exc)
            )

            return state