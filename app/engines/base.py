from abc import ABC, abstractmethod

class BaseEngine(ABC):
    @abstractmethod
    def analyze_audio(self, path: str):
        pass

    @abstractmethod
    def analyze_text(self, text: str):
        pass
