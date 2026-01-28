import pytest
from app.core.quran_repo import QuranRepo
from app.engines.text.tajweed_analyzer import TajweedAnalyzer


def test_text_analysis_real():
    repo = QuranRepo()
    engine = TajweedAnalyzer()

    quran_text = repo.get_ayah(1, 1)
    student_text = "الحمد لله رب العالمين"

    result = engine.analyze(
        expected_text=quran_text,
        input_text=student_text
    )

    assert isinstance(result, dict)
    assert "confidence" in result
    assert "mistakes" in result
