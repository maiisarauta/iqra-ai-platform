from app.engines.mock.audio import MockAudioEngine
from app.engines.mock.text import MockTextEngine


class EngineFactory:

    @staticmethod
    def get_audio_engine():
        return MockAudioEngine()

    @staticmethod
    def get_text_engine():
        return MockTextEngine()
