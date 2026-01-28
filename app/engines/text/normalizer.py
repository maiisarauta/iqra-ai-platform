import re

class ArabicNormalizer:
    """
    Normalize Arabic text for Qur'an comparison.
    Rule based and configurable.
    """

    HARAKAT_PATTERN = re.compile(r"[ًٌٍَُِّْـ]")
    TATWEEL = "ـ"

    ALEF_VARIANTS = {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
    }

    YA_VARIANTS = {
        "ى": "ي",
    }

    def normalize(self, text: str) -> str:
        if not text:
            return ""

        text = text.strip()

        # Remove tatweel
        text = text.replace(self.TATWEEL, "")

        # Normalize Alef
        for src, target in self.ALEF_VARIANTS.items():
            text = text.replace(src, target)

        # Normalize Ya
        for src, target in self.YA_VARIANTS.items():
            text = text.replace(src, target)

        # Remove harakat
        text = self.HARAKAT_PATTERN.sub("", text)

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text)

        return text
