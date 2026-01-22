from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_analyze_audio_success():
    payload = {
        "ayah_reference": "1:1",
        "audio_duration_seconds": 30
    }

    response = client.post("/analyze/audio", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["engine"] == "mock-audio"
    assert "confidence_score" in data
    assert 0 <= data["confidence_score"] <= 1
    assert isinstance(data["mistakes"], list)
    assert isinstance(data["corrections"], list)


def test_analyze_audio_duration_too_short():
    payload = {
        "ayah_reference": "1:1",
        "audio_duration_seconds": 5
    }

    response = client.post("/analyze/audio", json=payload)
    assert response.status_code == 422


def test_analyze_audio_duration_too_long():
    payload = {
        "ayah_reference": "1:1",
        "audio_duration_seconds": 4000
    }

    response = client.post("/analyze/audio", json=payload)
    assert response.status_code == 422
