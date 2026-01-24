def test_analyze_audio_success(client):
    response = client.post(
        "/analyze/audio",
        data={
            "surah": 1,
            "ayah": 1
        },
        files={
            "audio": ("test.wav", b"fake-audio")
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["surah"] == 1
    assert data["ayah"] == 1
    assert "confidence" in data
