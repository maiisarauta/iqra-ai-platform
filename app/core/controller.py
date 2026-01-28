from typing import Dict

from app.engines.audio.audio_engine import AudioEngine
from app.engines.text.tajweed_analyzer import TajweedAnalyzer
from app.engines.quran.sqlite_loader import QuranSQLiteLoader
from app.scoring.confidence import calculate_confidence

class Controller:
    """
    Iqra AI Orchestrator
    """

    def __init__(self):
        self.quran_repo = QuranSqliteLoader()
        self.audio_engine = AudioEngine()
        self.text_engine = TajweedAnalyzer()

    def analyze_text(self, surah: int, ayah: int, text: str) -> Dict:
        expected_text = self.quran_repo.get_ayah(surah, ayah)

        analysis = self.text_engine.analyze(
            expected_text=expected_text,
            input_text=text
        )

        confidence = calculate_confidence(
            total_units=len(expected_text.split()),
            text_mistakes=len(analysis["mistakes"]),
            tajweed_mistakes=len(analysis.get("tajweed", [])),
        )

        return {
            "surah": surah,
            "ayah": ayah,
            "confidence": confidence,
            "mistakes": analysis["mistakes"],
            "corrections": analysis.get("corrections", []),
        }

    def analyze_audio(self, surah: int, ayah: int, audio_bytes: bytes) -> Dict:
        asr_text, audio_features = self.audio_engine.analyze(audio_bytes)

        expected_text = self.quran_repo.get_ayah(surah, ayah)

        analysis = self.text_engine.analyze(
            expected_text=expected_text,
            input_text=asr_text
        )

        confidence = calculate_confidence(
            total_units=len(expected_text.split()),
            text_mistakes=len(analysis["mistakes"]),
            tajweed_mistakes=len(analysis.get("tajweed", [])),
            audio_quality=audio_features.get("clarity"),
        )

        return {
            "surah": surah,
            "ayah": ayah,
            "confidence": confidence,
            "mistakes": analysis["mistakes"],
            "corrections": analysis.get("corrections", []),
        }
