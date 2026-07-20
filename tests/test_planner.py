"""
Unit tests for Planner.
"""

from app.agent.planner import Planner
from app.agent.state import AgentState
from app.llm.schemas import LLMResponse


class FakeLLMService:
    """
    Fake LLM used for testing.
    """

    def generate_plan(self, user_request: str) -> LLMResponse:
        return LLMResponse(
        content="Fake execution plan",
        model="fake-gemini"
    )


class FailingLLMService:
    """
    Fake LLM that always fails.
    """

    def generate_plan(self, user_request: str):
        raise RuntimeError("Gemini unavailable")


def test_plan_success():
    """
    Planner should update the state
    when planning succeeds.
    """

    planner = Planner(
        llm_service=FakeLLMService()
    )

    state = AgentState(
        user_request="Write a project proposal"
    )

    result = planner.plan(state)

    assert result.status == "planned"

    assert (
        result.execution_plan
        == "Fake execution plan"
    )

    assert result.errors == []


def test_plan_failure():
    """
    Planner should handle LLM failures.
    """

    planner = Planner(
        llm_service=FailingLLMService()
    )

    state = AgentState(
        user_request="Write proposal"
    )

    result = planner.plan(state)

    assert result.status == "failed"

    assert len(result.errors) == 1

    assert (
        result.errors[0]
        == "Gemini unavailable"
    )