from app.scoring.confidence import compute_confidence

def test_confidence_weighting():
    score = compute_confidence(
        total_units=10,
        mistakes=2,
        corrections=1
    )

    assert 0.0 <= score <= 1.0
    assert score < 1.0
