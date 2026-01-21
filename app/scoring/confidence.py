from typing import List, Dict

PENALTIES = {
    "pronunciation": 5,
    "tajweed": 7,
    "elongation": 3,
    "spelling": 4,
    "skipped": 10,
}


def calculate_confidence(mistakes: List[Dict]) -> float:
    """
    Calculate confidence score between 0.0 and 1.0
    based on detected mistakes.
    """
    score = 100

    for mistake in mistakes:
        penalty = PENALTIES.get(mistake.get("type"), 2)
        score -= penalty

    if score < 0:
        score = 0

    return round(score / 100, 2)
