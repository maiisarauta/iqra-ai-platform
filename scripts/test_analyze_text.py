from app.engines.mock.text import MockTextEngine

engine = MockTextEngine()

result = engine.analyze(
    surah=1,
    ayah=1,
    text="سْمِ ٱللَّهِ لرَّحْمَـٰنِ ٱلرّحِيمِ"
)

print(result)
