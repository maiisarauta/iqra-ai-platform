import sqlite3
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "quran.db"
QURAN_JSON = DATA_DIR / "quran_full.json"


def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ayahs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            surah INTEGER NOT NULL,
            ayah INTEGER NOT NULL,
            text TEXT NOT NULL,
            UNIQUE(surah, ayah)
        )
    """)


def populate_ayahs(cursor, quran_data):
    for surah_num, ayahs in quran_data.items():
        for ayah_num, text in ayahs.items():
            cursor.execute(
                """
                INSERT OR IGNORE INTO ayahs (surah, ayah, text)
                VALUES (?, ?, ?)
                """,
                (int(surah_num), int(ayah_num), text)
            )


def build_database():
    DATA_DIR.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    create_tables(cursor)

    with open(QURAN_JSON, "r", encoding="utf-8") as f:
        quran_data = json.load(f)

    populate_ayahs(cursor, quran_data)

    conn.commit()
    conn.close()

    print("✅ Qur’an SQLite database created successfully.")


if __name__ == "__main__":
    build_database()
