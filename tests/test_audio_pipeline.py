import pytest
librosa = pytest.importorskip("librosa")

from app.engines.audio.audio_engine import AudioEngine


def test_audio_pipeline_real(tmp_path):
    audio_path = tmp_path / "test.wav"
    audio_path.write_bytes(b"RIFF....fakewavdata")

    engine = AudioEngine()
    result = engine.process(str(audio_path))

    assert isinstance(result, dict)
    assert "confidence" in result
    assert "mistakes" in result
    assert "corrections" in result
