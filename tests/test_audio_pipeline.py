import pytest
import shutil

librosa = pytest.importorskip("librosa")

if shutil.which("ffmpeg") is None:
    pytest.skip("ffmpeg not installed, skipping real audio test", allow_module_level=True)

from app.engines.audio.audio_engine import AudioEngine


def test_audio_pipeline_real(tmp_path):
    audio_path = tmp_path / "test.wav"

    audio_path.write_bytes(
        b"RIFF\x24\x00\x00\x00WAVEfmt "
        b"\x10\x00\x00\x00\x01\x00\x01\x00"
        b"\x40\x1f\x00\x00\x80\x3e\x00\x00"
        b"\x02\x00\x10\x00data\x00\x00\x00\x00"
    )

    engine = AudioEngine()
    result = engine.process(str(audio_path))

    assert isinstance(result, dict)
    assert "confidence" in result
    assert "mistakes" in result
    assert "corrections" in result
