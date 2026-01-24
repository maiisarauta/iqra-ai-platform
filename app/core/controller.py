from typing import Dict

from app.engines.mock.text import MockTextEngine
from app.engines.mock.audio import MockAudioEngine
from app.utils.text import normalize_arabic_text


# change engine later
TEXT_ENGINE = MockTextEngine()
AUDIO_ENGINE = MockAudioEngine()


def analyze_text_controller(
    surah: int,
    ayah: int,
    text: str
) -> Dict:
    """
    Orchestrates text analysis.
    """
    normalized_text = normalize_arabic_text(text)

    result = TEXT_ENGINE.analyze(
        surah=surah,
        ayah=ayah,
        text=normalized_text
    )

    return {
        "surah": surah,
        "ayah": ayah,
        "confidence": result["confidence"],
        "mistakes": result["mistakes"],
        "corrections": result["corrections"],
    }


def analyze_audio_controller(
    surah: int,
    ayah: int,
    audio_bytes: bytes
) -> Dict:
    """
    Orchestrates audio analysis.
    """
    result = AUDIO_ENGINE.analyze(
        surah=surah,
        ayah=ayah,
        audio_bytes=audio_bytes
    )

    return {
        "surah": surah,
        "ayah": ayah,
        "confidence": result["confidence"],
        "mistakes": result["mistakes"],
        "corrections": result["corrections"],
    }
