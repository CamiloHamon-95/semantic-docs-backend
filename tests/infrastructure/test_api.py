from fastapi.testclient import TestClient
from infrastructure.web.api import app


client = TestClient(app)


def test_create_document_endpoint():
    response = client.post("/documents", json={
        "title": "Test",
        "text": "Some content"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test"
