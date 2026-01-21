from app.scoring.confidence import calculate_confidence
from app.main import app

def test_confidence_no_mistakes():
    score = calculate_confidence([])
    assert score == 1.0


def test_confidence_with_mistakes():
    mistakes = [
        {"type": "tajweed"},
        {"type": "pronunciation"},
    ]
    score = calculate_confidence(mistakes)
    assert 0 < score < 1.0
