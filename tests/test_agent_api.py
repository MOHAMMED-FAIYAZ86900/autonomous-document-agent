"""
Tests for the Agent API.
"""

from fastapi.testclient import TestClient

from app.main import app
from app.agent.state import AgentState
import app.api.routers.agent as agent_router


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

    original = agent_router.agent

    agent_router.agent = FakeAgent()

    response = client.post(
        "/agent/run",
        json={
            "user_request": "Create an AI report."
        },
    )

    agent_router.agent = original

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "completed"
    assert body["generated_content"] == "Generated test document."
    assert body["reflection"] == "Looks good."


def test_agent_failure():

    original = agent_router.agent

    agent_router.agent = FakeFailedAgent()

    response = client.post(
        "/agent/run",
        json={
            "user_request": "Create report"
        },
    )

    agent_router.agent = original

    assert response.status_code == 500

    body = response.json()

    assert body["detail"] == ["Planner failed"]