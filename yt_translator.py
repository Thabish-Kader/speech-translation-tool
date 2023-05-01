from moviepy.editor import *
from googletrans import Translator

# Download YouTube video and extract audio

audio_filename = "audio.mp3"
video = VideoFileClip("ss.mp4")
audio = video.audio
audio.write_audiofile(audio_filename)

# Translate audio to German
translator = Translator()
audio_text = translator.translate(AudioFileClip(audio_filename).to_soundarray(), dest='de').text
print(audio_text)

# Delete audio file
os.remove(audio_filename)
