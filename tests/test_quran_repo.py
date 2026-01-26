from app.core.quran_repo import QuranRepo

def test_quran_ayah_exact():
    text = QuranRepo.get_ayah(1, 1)
    assert "بِسْمِ" in text

def test_quran_surah_112():
    text = QuranRepo.get_ayah(112, 1)
    assert "قُلْ هُوَ ٱللَّهُ" in text
