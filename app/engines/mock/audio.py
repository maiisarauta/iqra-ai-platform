class MockAudioEngine:
    def analyze(self, duration: int, ayah_reference: str) -> dict:
        return {
            "ayah_reference": ayah_reference,
            "confidence": 0.78,
            "tajweed_errors": [],
        }
