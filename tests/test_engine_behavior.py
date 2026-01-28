import pytest
from app.engines.audio.audio_engine import AudioEngine
from app.engines.text.tajweed_analyzer import TajweedAnalyzer


def test_audio_engine_instantiation():
    engine = AudioEngine()
    assert engine is not None


def test_text_engine_instantiation():
    engine = TajweedAnalyzer()
    assert engine is not None


def test_engine_returns_expected_shape():
    engine = TajweedAnalyzer()

    result = engine.analyze(
        expected_text="ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ",
        input_text="الحمد لله رب العالمين"
    )

    assert isinstance(result, dict)
    assert "confidence" in result
    assert "mistakes" in result
