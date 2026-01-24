import json
from pathlib import Path
from typing import Dict


class QuranRepo:
    """
    Today: JSON
    Lster: SQLite
    """

    _DATA_PATH = Path(__file__).resolve().parent.parent / "engines" / "quran" / "data"
    _CACHE: Dict[int, Dict] = {}

    @classmethod
    def _load_surah(cls, surah: int) -> Dict:
        if surah in cls._CACHE:
            return cls._CACHE[surah]

        file_path = cls._DATA_PATH / f"surah_{surah}.json"

        if not file_path.exists():
            raise ValueError(f"Surah {surah} not found in Qur’an data")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        cls._CACHE[surah] = data
        return data

    @classmethod
    def get_ayah(cls, surah: int, ayah: int) -> str:
        surah_data = cls._load_surah(surah)

        ayahs = surah_data.get("ayahs", {})
        ayah_text = ayahs.get(str(ayah))

        if not ayah_text:
            raise ValueError(f"Ayah {ayah} not found in Surah {surah}")

        return ayah_text
