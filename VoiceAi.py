from pydub import AudioSegment
import os

for file in os.listdir("."):
    if file.endswith(".wav"):
        if not file.startswith("NW_"):
            sound = AudioSegment.from_wav(file)
            sound = sound[:-1800]
            sound.export("NW_" + file, format="wav")