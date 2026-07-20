"""
Unit tests for AgentOrchestrator.
"""

from app.agent.orchestrator import AgentOrchestrator
from app.agent.state import AgentState


class FakePlanner:
    def plan(self, state: AgentState) -> AgentState:
        state.execution_plan = "Fake execution plan"
        state.status = "planned"
        return state


class FakeExecutor:
    def execute(self, state: AgentState) -> AgentState:
        state.generated_content = "Generated document"
        state.status = "executed"
        return state


class FakeReflector:
    def review(self, state: AgentState) -> AgentState:
        state.reflection = "Looks good"
        state.status = "reviewed"
        return state


class FailingPlanner:
    def plan(self, state: AgentState) -> AgentState:
        state.status = "failed"
        state.errors.append("Planning failed")
        return state


def test_orchestrator_success():
    """
    Entire workflow should complete successfully.
    """

    orchestrator = AgentOrchestrator()

    orchestrator.planner = FakePlanner()
    orchestrator.executor = FakeExecutor()
    orchestrator.reflector = FakeReflector()

    result = orchestrator.run("Create a project proposal")

    assert result.status == "completed"
    assert result.execution_plan == "Fake execution plan"
    assert result.generated_content == "Generated document"
    assert result.reflection == "Looks good"
    assert result.errors == []


def test_orchestrator_planner_failure():
    """
    Workflow should stop if planning fails.
    """

    orchestrator = AgentOrchestrator()

    orchestrator.planner = FailingPlanner()
    orchestrator.executor = FakeExecutor()
    orchestrator.reflector = FakeReflector()

    result = orchestrator.run("Create proposal")

    assert result.status == "failed"
    assert result.errors == ["Planning failed"]

    assert result.generated_content is None
    assert result.reflection is None