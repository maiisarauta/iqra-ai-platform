from abc import ABC, abstractmethod

class BaseAudioEngine(ABC):

    @abstractmethod
    async def analyze(self, *, ayah_ref: str) -> dict:
        pass


class BaseTextEngine(ABC):

    @abstractmethod
    async def analyze(self, *, text: str, ayah_ref: str) -> dict:
        pass
