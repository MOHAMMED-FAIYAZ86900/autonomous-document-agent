"""
Unit tests for Reflector.
"""

from app.agent.reflector import Reflector
from app.agent.state import AgentState
from app.llm.schemas import LLMResponse


class FakeLLMService:
    """
    Fake LLM used for testing.
    """

    def review_document(
        self,
        document: str,
    ) -> LLMResponse:
        return LLMResponse(
            content="Document looks good with minor improvements.",
            model="fake-gemini",
        )


class FailingLLMService:
    """
    Fake LLM that always fails.
    """

    def review_document(
        self,
        document: str,
    ):
        raise RuntimeError(
            "Reflection failed"
        )


def test_review_success():
    """
    Reflector should review
    the generated document successfully.
    """

    reflector = Reflector(
        llm_service=FakeLLMService()
    )

    state = AgentState(
        user_request="Create proposal",
        generated_content="Generated proposal content",
    )

    result = reflector.review(state)

    assert result.status == "reviewed"

    assert (
        result.reflection
        == "Document looks good with minor improvements."
    )

    assert result.errors == []


def test_review_failure():
    """
    Reflector should handle
    LLM failures gracefully.
    """

    reflector = Reflector(
        llm_service=FailingLLMService()
    )

    state = AgentState(
        user_request="Create proposal",
        generated_content="Generated proposal content",
    )

    result = reflector.review(state)

    assert result.status == "failed"

    assert len(result.errors) == 1

    assert (
        result.errors[0]
        == "Reflection failed"
    )