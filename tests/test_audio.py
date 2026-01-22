def test_analyze_audio_success(client):
    payload = {
        "ayah_reference": "1:1"
    }

    files = {
        "audio": ("test.wav", b"fake-audio-bytes", "audio/wav")
    }

    response = client.post(
        "/analyze/audio",
        data=payload,
        files=files
    )

    assert response.status_code == 200

    data = response.json()
    assert data["engine"] == "mock-audio"
    assert isinstance(data["confidence_score"], float)
