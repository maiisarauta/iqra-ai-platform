from app.engines.text.normalizer import ArabicNormalizer
from app.engines.text.comparator import TextComparator

class TajweedAnalyzer:
    """
    Tajweed & Arabic correctness analyzer.
    """

    def __init__(self):
        self.normalizer = ArabicNormalizer()
        self.comparator = TextComparator()

    def analyze(self, expected_text: str, input_text: str) -> dict:
        normalized_expected = self.normalizer.normalize(expected_text)
        normalized_input = self.normalizer.normalize(input_text)

        comparison = self.comparator.compare(
            normalized_expected,
            normalized_input
        )

        confidence = comparison["similarity"]

        return {
            "expected": expected_text,
            "input": input_text,
            "normalized_expected": normalized_expected,
            "normalized_input": normalized_input,
            "confidence": confidence,
            "mistakes": comparison["differences"],
        }
