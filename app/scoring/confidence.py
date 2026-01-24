def compute_confidence(
    total_units: int,
    mistakes: int,
    corrections: int,
    mistake_weight: float = 1.0,
    correction_weight: float = 0.5,
) -> float:

    penalty = (mistakes * mistake_weight) + (corrections * correction_weight)

    raw_score = 1.0 - (penalty / max(total_units, 1))

    return round(max(0.0, min(1.0, raw_score)), 3)

def calculate_confidence(
    mistakes: int,
    total_units: int,
    corrections: int = 0,
) -> float:

    return compute_confidence(
        total_units=total_units,
        mistakes=mistakes,
        corrections=corrections,
    )
