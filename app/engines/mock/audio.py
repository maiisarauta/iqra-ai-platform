class MockAudioEngine:

    def analyze(self, audio_bytes: bytes, ayah_reference: str) -> dict:
        return {
            "engine": "mock-audio",
            "mistakes": [],
            "corrections": [],
            "confidence_score": 0.78
        }
