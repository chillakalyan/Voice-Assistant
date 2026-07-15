import sounddevice as sd
import soundfile as sf

def play_audio(filename):
    data, fs = sf.read(filename)

    sd.play(data, fs)
    sd.wait()