from difflib import SequenceMatcher

class TextComparator:
    """
    Compare expected Qur'an text with input text.
    """

    def compare(self, expected: str, actual: str) -> dict:
        matcher = SequenceMatcher(None, expected, actual)

        similarity = matcher.ratio()

        differences = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != "equal":
                differences.append({
                    "type": tag,
                    "expected": expected[i1:i2],
                    "found": actual[j1:j2],
                })

        return {
            "similarity": round(similarity, 4),
            "differences": differences,
        }
