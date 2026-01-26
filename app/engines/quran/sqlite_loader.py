import sqlite3
from pathlib import Path


class QuranSQLiteLoader:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)

    def get_ayah(self, surah: int, ayah: int) -> str:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT text FROM ayahs WHERE surah = ? AND ayah = ?",
            (surah, ayah)
        )

        row = cursor.fetchone()
        conn.close()

        if row is None:
            raise LookupError(f"Ayah not found: {surah}:{ayah}")

        return row[0]
