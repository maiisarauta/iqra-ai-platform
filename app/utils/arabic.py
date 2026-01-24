import re

HARAKAT_PATTERN = re.compile(
    r"[\u064B-\u0652\u0670]"
)

def remove_harakat(text: str) -> str:
    """Remove tashkeel / harakat from Arabic text"""
    return HARAKAT_PATTERN.sub("", text)


def normalize_arabic(text: str) -> str:
    """
    Normalize Arabic for comparison:
    - Remove harakat
    - Normalize alef forms
    - Normalize yaa / alif maqsurah
    """
    text = remove_harakat(text)

    replacements = {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ى": "ي",
        "ؤ": "و",
        "ئ": "ي",
    }

    for src, target in replacements.items():
        text = text.replace(src, target)

    return text.strip()
