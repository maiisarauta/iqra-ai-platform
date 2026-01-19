from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_text_success():
    response = client.post(
        "/analyze/text",
        json={
            "ayah_ref": "1:1",
            "text": "Bismillahir Rahmanir Rahim"
        }
    )
    assert response.status_code == 200
    body = response.json()

    assert "confidence_score" in body
    assert "engine" in body
    assert body["engine"] == "mock-text"
