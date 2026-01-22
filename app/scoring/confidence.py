def calculate_confidence(
    total_items: int,
    mistakes: int,
    corrections: int
) -> float:
    """
    Simple confidence scoring logic.

    - total_items: number of expected words/phonemes
    - mistakes: number of detected mistakes
    - corrections: number of suggested corrections
    """

    if total_items <= 0:
        return 0.0

    penalty = mistakes + (corrections * 0.5)
    score = max(0.0, 1.0 - (penalty / total_items))

    return round(score, 2)
