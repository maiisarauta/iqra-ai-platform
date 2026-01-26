from app.engines.text.tajweed_analyzer import TajweedAnalyzer

def test_simple_normalization():
    analyzer = TajweedAnalyzer()

    result = analyzer.analyze(
        "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ",
        "بسم الله الرحمن"
    )

    assert result["confidence"] >= 0.7
