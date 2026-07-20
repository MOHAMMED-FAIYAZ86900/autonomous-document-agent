"""
Unit tests for Executor.
"""

from app.agent.executor import Executor
from app.agent.state import AgentState
from app.llm.schemas import LLMResponse


class FakeLLMService:
    """
    Fake LLM used for testing.
    """

    def generate_document(
        self,
        execution_plan: str,
    ) -> LLMResponse:
        return LLMResponse(
            content="Generated proposal document",
            model="fake-gemini",
        )


class FailingLLMService:
    """
    Fake LLM that always fails.
    """

    def generate_document(
        self,
        execution_plan: str,
    ):
        raise RuntimeError(
            "Document generation failed"
        )


def test_execute_success():
    """
    Executor should generate
    document successfully.
    """

    executor = Executor(
        llm_service=FakeLLMService()
    )

    state = AgentState(
        user_request="Create proposal",
        execution_plan="Write introduction and scope",
    )

    result = executor.execute(state)

    assert result.status == "executed"

    assert (
        result.generated_content
        == "Generated proposal document"
    )

    assert result.errors == []


def test_execute_failure():
    """
    Executor should handle
    LLM failures.
    """

    executor = Executor(
        llm_service=FailingLLMService()
    )

    state = AgentState(
        user_request="Create proposal",
        execution_plan="Write proposal",
    )

    result = executor.execute(state)

    assert result.status == "failed"

    assert len(result.errors) == 1

    assert (
        result.errors[0]
        == "Document generation failed"
    )