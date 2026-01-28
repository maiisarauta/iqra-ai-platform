def compute_confidence(
    total_units: int,
    mistakes: int,
    corrections: int,
    mistake_weight: float = 1.0,
    correction_weight: float = 0.5,
    audio_penalty: float = 0.0,
) -> float:
    """
    Compute confidence score between 0 and 1.
    """

    penalty = (mistakes * mistake_weight) + (corrections * correction_weight)
    penalty += audio_penalty

    raw_score = 1.0 - (penalty / max(total_units, 1))

    return round(max(0.0, min(1.0, raw_score)), 4)


def calculate_confidence(
    total_units: int,
    text_mistakes: int,
    tajweed_mistakes: int = 0,
    corrections: int = 0,
    audio_quality: float | None = None,
) -> float:
    """
    Unified confidence calculation for Iqra AI.
    """

    audio_penalty = 0.0
    if audio_quality is not None and audio_quality < 0.6:
        audio_penalty = 0.2

    return compute_confidence(
        total_units=total_units,
        mistakes=text_mistakes + tajweed_mistakes,
        corrections=corrections,
        audio_penalty=audio_penalty,
    )
