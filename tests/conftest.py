import sqlite3
import pytest
from pathlib import Path

from app.engines.quran.sqlite_loader import QuranSQLiteLoader
from app.core.quran_repo import QuranRepo


@pytest.fixture(scope="session")
def test_db_path(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("db") / "test_quran.db"

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE ayahs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surah INTEGER NOT NULL,
        ayah INTEGER NOT NULL,
        text TEXT NOT NULL,
        UNIQUE(surah, ayah)
    );
    """)

    # minimal test data
    cur.executemany(
        "INSERT INTO ayahs (surah, ayah, text) VALUES (?, ?, ?)",
        [
            (1, 1, "بِسْمِ ٱللَّهِ"),
            (1, 2, "ٱلْحَمْدُ لِلَّهِ"),
            (112, 1, "قُلْ هُوَ ٱللَّهُ أَحَدٌ"),
        ]
    )

    conn.commit()
    conn.close()

    return db_path


@pytest.fixture
def quran_repo(test_db_path):
    loader = QuranSQLiteLoader(db_path=test_db_path)
    return QuranRepo(loader=loader)
