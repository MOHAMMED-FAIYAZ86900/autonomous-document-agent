"""
Tests for the Agent API.
"""

from fastapi.testclient import TestClient

from app.agent.state import AgentState
from app.api.routers.agent import get_agent
from app.main import app

client = TestClient(app)


class FakeAgent:
    def run(self, request: str):

        state = AgentState(user_request=request)
        state.status = "completed"
        state.generated_content = "Generated test document."
        state.reflection = "Looks good."

        return state


class FakeFailedAgent:
    def run(self, request: str):

        state = AgentState(user_request=request)
        state.status = "failed"
        state.errors = ["Planner failed"]

        return state


def test_agent_success():

    app.dependency_overrides[get_agent] = lambda: FakeAgent()

    response = client.post(
        "/agent/run",
        json={"user_request": "Create an AI report."},
    )

    app.dependency_overrides.clear()

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "completed"
    assert body["generated_content"] == "Generated test document."
    assert body["reflection"] == "Looks good."


def test_agent_failure():

    app.dependency_overrides[get_agent] = lambda: FakeFailedAgent()

    response = client.post(
        "/agent/run",
        json={"user_request": "Create report"},
    )

    app.dependency_overrides.clear()

    assert response.status_code == 500

    body = response.json()

    assert body["detail"] == ["Planner failed"]
