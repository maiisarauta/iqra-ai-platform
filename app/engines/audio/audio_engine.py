from app.engines.audio.audio_loader import load_audio
from app.engines.audio.audio_normalizer import AudioNormalizer
from app.engines.audio.audio_features import AudioFeatureExtractor
from app.engines.audio.audio_to_text import speech_to_text

class AudioEngine:
    def process(self, audio_path: str):
        waveform, sr = load_audio(audio_path)
        clean = normalize_audio(waveform)
        features = extract_features(clean, sr)
        text = speech_to_text(clean, sr)

        return text, features
