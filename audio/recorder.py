
import os
from datetime import datetime

import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000


def record_audio(duration=30):

    os.makedirs("recordings", exist_ok=True)

    filename = (
        f"recordings/"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    )

    print("🎤 Listening...")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(filename, audio, SAMPLE_RATE)

    print(f"✅ Saved to {filename}")

    return filename