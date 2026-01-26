import json
from pathlib import Path
from typing import Dict, Optional

from pathlib import Path
from app.engines.quran.sqlite_loader import QuranSQLiteLoader


class QuranRepo:
    """
    Qur’an Repository

    Single source of SQLite

    - Provide ayah text to engines
    - Prepare for future upgrade
    """

    _loader = None

    @classmethod
    def _get_db_path(cls) -> Path:
        """
        Path to quran.db
        """
        return (
            Path(__file__)
            .resolve()
            .parents[2]
            / "data"
            / "quran.db"
        )

    @classmethod
    def _get_loader(cls) -> QuranSQLiteLoader:
        """
        Lazy-load SQLite loader
        """
        if cls._loader is None:
            db_path = cls._get_db_path()
            cls._loader = QuranSQLiteLoader(db_path=db_path)
        return cls._loader

    @classmethod
    def get_ayah(cls, surah: int, ayah: int) -> str:
        """
        Fetch ayah text from SQLite Qur’an database.
        """
        return cls._get_loader().get_ayah(surah, ayah)

