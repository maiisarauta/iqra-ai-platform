from app.core.engine import EngineFactory


class AnalysisController:

    @staticmethod
    def analyze_audio(audio_bytes: bytes, ayah_reference: str) -> dict:
        engine = EngineFactory.get_audio_engine()
        return engine.analyze(audio_bytes, ayah_reference)

    @staticmethod
    def analyze_text(text: str, ayah_reference: str) -> dict:
        engine = EngineFactory.get_text_engine()
        return engine.analyze(text, ayah_reference)
