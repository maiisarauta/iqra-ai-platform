from app.core.quran_repo import QuranRepo

def test_quran_ayah_exact():
    ayah = QuranRepo.get_ayah(1, 1)
    assert ayah == "بسم الله الرحمن الرحيم"


def test_quran_surah_112():
    ayah = QuranRepo.get_ayah(112, 4)
    assert ayah.endswith("أحد")
