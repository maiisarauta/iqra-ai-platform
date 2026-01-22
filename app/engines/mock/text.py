class MockTextEngine:

    def analyze(self, text: str, ayah_reference: str) -> dict:
        return {
            "engine": "mock-text",
            "mistakes": ["missing madd"],
            "corrections": ["add madd on الرحمن"],
            "confidence_score": 0.82
        }
