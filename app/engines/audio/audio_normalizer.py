class AudioNormalizer:
    @staticmethod
    def normalize(audio_path):
        """
        Future:
        - resample to 16kHz
        - mono
        - trim silence
        """
        return {
            "path": audio_path,
            "sample_rate": 16000,
            "channels": 1,
            "duration": 3.2
        }
