from app.engines.audio.audio_loader import AudioLoader
from app.engines.audio.audio_normalizer import AudioNormalizer
from app.engines.audio.audio_features import AudioFeatureExtractor
from app.engines.audio.audio_to_text import AudioToTextAdapter

class AudioEngine:
    def analyze(self, audio_path: str) -> str:
        path = AudioLoader.load(audio_path)
        normalized = AudioNormalizer.normalize(path)
        features = AudioFeatureExtractor.extract(normalized)
        text = AudioToTextAdapter.transcribe(features)
        return text
