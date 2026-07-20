"""
Tests for the Documents API.
"""

from pathlib import Path

from fastapi.testclient import TestClient

import app.api.routers.documents as documents_router
from app.main import app

client = TestClient(app)


class FakeStorage:
    def list_documents(self):
        return []

    def exists(self, filename):
        return filename == "sample.docx"

    def get_path(self, filename):
        return Path(__file__).parent / "sample.docx"


def test_list_documents():

    original = documents_router.storage

    documents_router.storage = FakeStorage()

    response = client.get("/documents")

    documents_router.storage = original

    assert response.status_code == 200
    assert response.json() == []


def test_document_not_found():

    original = documents_router.storage

    documents_router.storage = FakeStorage()

    response = client.get("/documents/missing.docx")

    documents_router.storage = original

    assert response.status_code == 404
    assert response.json()["detail"] == "Document not found."
