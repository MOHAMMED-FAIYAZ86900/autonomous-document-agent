"""
Agent orchestrator for the Autonomous Document Agent.
"""

from app.agent.executor import Executor
from app.agent.planner import Planner
from app.agent.reflector import Reflector
from app.agent.state import AgentState
from app.core.logging import get_logger
from app.document.generator import DocumentGenerator


class AgentOrchestrator:
    """
    Coordinates the complete autonomous workflow.
    """

    def __init__(self) -> None:
        self.logger = get_logger(__name__)

        self.planner = Planner()
        self.executor = Executor()
        self.generator = DocumentGenerator()
        self.reflector = Reflector()

    def run(
        self,
        user_request: str,
    ) -> AgentState:
        """
        Execute the complete autonomous workflow.
        """

        self.logger.info("Agent execution started.")

        state = AgentState(
            user_request=user_request
        )

        # Step 1: Planning
        state = self.planner.plan(state)

        if state.status == "failed":
            return state

        # Step 2: Generate AI content
        state = self.executor.execute(state)

        if state.status == "failed":
            return state

        # Step 3: Generate DOCX
        state = self.generator.generate(state)

        if state.status == "failed":
            return state

        # Step 4: Reflection
        state = self.reflector.review(state)

        if state.status == "failed":
            return state

        state.status = "completed"

        self.logger.info(
            "Agent execution completed."
        )

        return state