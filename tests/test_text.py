def test_analyze_text_success(client):
    payload = {
        "surah": 1,
        "ayah": 1,
        "text": "بسم الله الرحمن الرحيم"
    }

    response = client.post("/analyze/text", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["surah"] == 1
    assert data["ayah"] == 1
    assert "confidence" in data
    assert "mistakes" in data
    assert "corrections" in data
