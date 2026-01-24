from app.engines.mock.text import MockTextEngine

def test_engine_returns_expected_shape():
    engine = MockTextEngine()

    result = engine.analyze(
        surah=1,
        ayah=1,
        text="بسم الله الرحمن الرحيم"
    )

    assert "confidence" in result
    assert "mistakes" in result
    assert "corrections" in result
    assert result["surah"] == 1
    assert result["ayah"] == 1
