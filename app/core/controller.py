from app.engines.mock.audio import MockAudioEngine
from app.engines.mock.text import MockTextEngine

audio_engine = MockAudioEngine()
text_engine = MockTextEngine()


async def analyze_audio(*, ayah_ref: str) -> dict:
    return await audio_engine.analyze(ayah_ref=ayah_ref)


async def analyze_text(*, text: str, ayah_ref: str) -> dict:
    return await text_engine.analyze(text=text, ayah_ref=ayah_ref)
