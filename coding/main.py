from os import path
from pydub import AudioSegment

# # files
# src = "horvath.mp3"
# dst = "test.wav"
#
# # convert wav to mp3
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

# import required modules
import subprocess

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', 'horvath.mp3',
                 'converted_to_wav_file.wav'])