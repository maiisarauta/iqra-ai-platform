class MockTextEngine:
    def analyze(self, text: str, ayah_reference: str) -> dict:
        return {
            "ayah_reference": ayah_reference,
            "match_score": 0.85,
            "mistakes": [],
            "normalized_text": text.strip(),
        }
