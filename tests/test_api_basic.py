"""
Basic FastAPI endpoint tests.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    """
    Test root endpoint.
    """

    response = client.get("/")

    assert response.status_code == 200

    body = response.json()

    assert "message" in body
    assert "version" in body
    assert "docs" in body
    assert "health" in body


def test_health():
    """
    Test health endpoint.
    """

    response = client.get("/health/")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"

    assert "application" in body
    assert "version" in body
    assert "environment" in body
