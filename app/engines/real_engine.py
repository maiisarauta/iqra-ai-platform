from app.engines.base import BaseEngine
from app.engines.audio.audio_engine import AudioEngine
from app.engines.text.normalizer import normalize
from app.engines.text.comparator import compare
from app.engines.text.tajweed_analyzer import analyze
from app.engines.quran.sqlite_loader import QuranRepository
from app.scoring.confidence import calculate

class RealEngine(BaseEngine):
    def __init__(self):
        self.audio = AudioEngine()
        self.quran = QuranRepository()

    def analyze_audio(self, path: str):
        text, features = self.audio.process(path)
        return self._analyze_text(text, features)

    def analyze_text(self, text: str):
        return self._analyze_text(text)

    def _analyze_text(self, text, features=None):
        normalized = normalize(text)
        ayah = self.quran.find_best_match(normalized)

        text_errors = compare(normalized, ayah)
        tajweed_errors = analyze(normalized)

        confidence = calculate(text_errors, tajweed_errors, features)

        return {
            "ayah": ayah,
            "text_errors": text_errors,
            "tajweed_errors": tajweed_errors,
            "confidence": confidence
        }
