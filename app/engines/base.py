from abc import ABC, abstractmethod


class BaseEngine(ABC):

    @abstractmethod
    def analyze_audio(self, audio_bytes: bytes, ayah_reference: str) -> dict:
        pass

    @abstractmethod
    def analyze_text(self, text: str, ayah_reference: str) -> dict:
        pass
