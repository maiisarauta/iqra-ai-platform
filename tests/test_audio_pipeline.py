from app.engines.audio.audio_engine import AudioEngine

def test_audio_pipeline_mock(tmp_path):
    audio = tmp_path / "test.wav"
    audio.write_bytes(b"FAKE_AUDIO")

    engine = AudioEngine()
    text = engine.analyze(str(audio))

    assert isinstance(text, str)
    assert len(text) > 0
