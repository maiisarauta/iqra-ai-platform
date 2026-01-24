from app.utils.arabic import normalize_arabic

def tokenize(text: str) -> list[str]:
    """
    Normalize and split Arabic text into tokens (words)
    """
    normalized = normalize_arabic(text)
    return normalized.split()

def normalize_arabic_text(text: str) -> str:
    """
    Adapter function used by controller.
    Keeps text normalization logic centralized.
    """
    return normalize_arabic(text)
