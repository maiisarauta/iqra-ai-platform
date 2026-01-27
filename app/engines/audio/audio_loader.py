from pathlib import Path

class AudioLoader:
    SUPPORTED_FORMATS = {".wav", ".mp3", ".ogg"}

    @staticmethod
    def load(audio_path: str) -> Path:
        path = Path(audio_path)

        if not path.exists():
            raise FileNotFoundError("Audio file not found")

        if path.suffix.lower() not in AudioLoader.SUPPORTED_FORMATS:
            raise ValueError("Unsupported audio format")

        return path
