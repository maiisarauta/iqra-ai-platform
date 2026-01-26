from app.core.quran_repo import QuranRepo


def test_quran_ayah_exact():
    text = QuranRepo.get_ayah(1, 1)

    assert isinstance(text, str)
    assert len(text) > 10
    assert "ٱللَّه" in text or "الله" in text


def test_quran_surah_112():
    ayah1 = QuranRepo.get_ayah(112, 1)

    assert isinstance(ayah1, str)
    assert len(ayah1) > 5
