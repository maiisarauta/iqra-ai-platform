from typing import Dict

from app.engines.base import BaseEngine
from app.core.quran_repo import QuranRepo
from app.core.text_compare import compare_text
from app.scoring.confidence import calculate_confidence


class MockTextEngine(BaseEngine):

    def analyze(self, surah: int, ayah: int, text: str) -> Dict:
        reference_text = QuranRepo.get_ayah(surah, ayah)

        comparison = compare_text(
            reference=reference_text,
            input_text=text
        )

        return {
            "surah": surah,
            "ayah": ayah,
            "confidence": comparison["confidence"],
            "mistakes": comparison["mistakes"],
            "corrections": comparison["corrections"],
        }
