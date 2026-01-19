class MockAudioEngine:
    async def analyze(self, *, ayah_ref: str) -> dict:
        return {
            "mistakes": ["mock: pronunciation issue"],
            "corrections": ["mock: correct articulation"],
            "confidence_score": 0.78
        }
