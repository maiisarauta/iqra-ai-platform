from app.core.quran_repo import QuranRepo
from app.engines.mock.text import MockTextEngine


def test_analyze_text_with_sqlite_quran():
    engine = MockTextEngine()
    engine.quran_repo = QuranRepo

    result = engine.analyze(
        surah=1,
        ayah=1,
        text="بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ"
    )

    assert result["surah"] == 1
    assert result["ayah"] == 1
    assert result["confidence"] > 0.9
    assert result["mistakes"] == []
