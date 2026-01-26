from app.core.controller import analyze_text_controller


def test_analyze_text_with_sqlite_quran():
    result = analyze_text_controller(
        text="بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
        surah=1,
        ayah=1,
    )

    assert result["surah"] == 1
    assert result["ayah"] == 1
    assert "confidence" in result
    assert 0 <= result["confidence"] <= 1
    assert isinstance(result["mistakes"], list)
    assert isinstance(result["corrections"], list)
