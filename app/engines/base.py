from abc import ABC, abstractmethod
from typing import Dict


class BaseEngine(ABC):

    @abstractmethod
    def analyze(self, **kwargs) -> Dict:
        """
        Every engine MUST return:
        {
          confidence: float,
          mistakes: list,
          corrections: list
        }
        """
        pass
