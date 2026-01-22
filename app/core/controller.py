from app.engines.mock.audio import MockAudioEngine
from app.engines.mock.text import MockTextEngine

audio_engine = MockAudioEngine()
text_engine = MockTextEngine()


def analyze_text(text: str, ayah_reference: str) -> dict:
    return text_engine.analyze(text, ayah_reference)


def analyze_audio(duration: int, ayah_reference: str) -> dict:
    return audio_engine.analyze(duration, ayah_reference)
