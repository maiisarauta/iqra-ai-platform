import subprocess
import tempfile

def load_audio(path: str):
    import librosa
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    subprocess.run(
        ["ffmpeg", "-y", "-i", path, "-ar", "16000", "-ac", "1", tmp.name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return librosa.load(tmp.name, sr=16000)
