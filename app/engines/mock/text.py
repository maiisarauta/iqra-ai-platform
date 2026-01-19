class MockTextEngine:
    async def analyze(self, *, text: str, ayah_ref: str) -> dict:
        return {
            "mistakes": ["mock: spelling error"],
            "corrections": ["mock: corrected spelling"],
            "confidence_score": 0.88
        }
