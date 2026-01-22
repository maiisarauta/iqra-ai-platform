from app.scoring.confidence import calculate_confidence


def test_confidence_perfect():
    score = calculate_confidence(
        total_items=10,
        mistakes=0,
        corrections=0
    )
    assert score == 1.0


def test_confidence_with_errors():
    score = calculate_confidence(
        total_items=10,
        mistakes=2,
        corrections=2
    )
    assert score < 1.0
