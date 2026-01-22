def test_analyze_text_success(client):
    payload = {
        "ayah_reference": "1:1",
        "text": "بسم الله الرحمن الرحيم"
    }

    response = client.post("/analyze/text", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "engine" in data
    assert "mistakes" in data
    assert "corrections" in data
    assert "confidence_score" in data
