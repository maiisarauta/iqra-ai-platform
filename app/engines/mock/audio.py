from typing import Dict

from app.engines.base import BaseEngine
from app.engines.mock.text import MockTextEngine
from app.utils.audio import mock_asr_transcribe


class MockAudioEngine(BaseEngine):
    # Audio engine currently

    def analyze(self, surah: int, ayah: int, audio_bytes: bytes) -> Dict:
        # Mock for now, future: Whisper
        transcribed_text = mock_asr_transcribe(audio_bytes)

        text_engine = MockTextEngine()

        return text_engine.analyze(
            surah=surah,
            ayah=ayah,
            text=transcribed_text
        )
