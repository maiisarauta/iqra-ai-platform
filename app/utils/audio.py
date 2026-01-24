def audio_bytes_to_text(audio_bytes: bytes) -> str:
    """
    Placeholder for ASR.
    Today: mock
    Tomorrow: Whisper/DeepSpeech
    """
    return "بسم الله الرحمن الرحيم"

def mock_asr_transcribe(audio_bytes: bytes | None = None) -> str:
    """
    Adapter for mock audio engine.
    Keeps engine imports stable.
    """
    if audio_bytes is None:
        return "بسم الله الرحمن الرحيم"

    return audio_bytes_to_text(audio_bytes)
