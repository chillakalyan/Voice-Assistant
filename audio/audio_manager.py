import sounddevice as sd
import soundfile as sf


class AudioManager:

    SAMPLE_RATE = 16000

    def record(self, duration, filename):

        print("Listening...")

        audio = sd.rec(
            int(duration * self.SAMPLE_RATE),
            samplerate=self.SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(filename, audio, self.SAMPLE_RATE)

        print("Recording saved.")

    def play(self, filename):

        data, fs = sf.read(filename)

        sd.play(data, fs)
        sd.wait()