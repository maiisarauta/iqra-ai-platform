from abc import ABC, abstractmethod


class TextEngine(ABC):
    @abstractmethod
    def analyze(self, text: str, ayah_reference: str) -> dict:
        pass


class AudioEngine(ABC):
    @abstractmethod
    def analyze(self, duration: int, ayah_reference: str) -> dict:
        pass
