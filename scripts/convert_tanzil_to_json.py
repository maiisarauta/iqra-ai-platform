import json
from pathlib import Path


INPUT_FILE = Path("data/quran_tanzil_uthmani.txt")
OUTPUT_FILE = Path("data/quran_full.json")


def convert():
    quran = {}

    with INPUT_FILE.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Skip comments / copyright
            if line.startswith("#"):
                continue

            # Skip invalid lines
            if "|" not in line:
                continue

            try:
                surah, ayah, text = line.split("|", 2)
            except ValueError:
                raise ValueError(f"Invalid format at line {line_no}: {line}")

            quran.setdefault(surah, {})[ayah] = text

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(quran, f, ensure_ascii=False, indent=2)

    print("✅ Qur’an successfully converted to JSON!")


if __name__ == "__main__":
    convert()
