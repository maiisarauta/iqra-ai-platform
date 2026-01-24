from app.utils.text import tokenize
from app.scoring.confidence import compute_confidence


def compare_text(
    reference_text: str | None = None,
    input_text: str | None = None,
    **kwargs
):
    """
    Compare reference Qur'an text with input text.
    Accepts keyword aliases for flexibility.
    """

    if reference_text is None:
        reference_text = kwargs.get("reference")

    if input_text is None:
        input_text = kwargs.get("text") or kwargs.get("input")

    if not reference_text or not input_text:
        raise ValueError("Both reference_text and input_text are required")

    ref_tokens = tokenize(reference_text)
    input_tokens = tokenize(input_text)

    mistakes = []
    corrections = []

    max_len = max(len(ref_tokens), len(input_tokens))

    for i in range(max_len):
        ref_word = ref_tokens[i] if i < len(ref_tokens) else None
        input_word = input_tokens[i] if i < len(input_tokens) else None

        if ref_word != input_word:
            if ref_word and not input_word:
                mistakes.append({
                    "type": "missing_word",
                    "expected": ref_word,
                    "found": input_word,
                    "position": i
                })
            else:
                corrections.append({
                    "type": "wrong_word",
                    "expected": ref_word,
                    "found": input_word,
                    "position": i
                })

    total_units = max(len(ref_tokens), 1)

    confidence = compute_confidence(
        total_units=total_units,
        mistakes=len(mistakes),
        corrections=len(corrections)
    )

    return {
        "mistakes": mistakes,
        "corrections": corrections,
        "confidence": confidence
    }
