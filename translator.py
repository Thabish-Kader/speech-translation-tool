import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

r = sr.Recognizer()
# get audio from the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source,timeout=2, phrase_time_limit=5)
    print("Done")

# get text from audio
audio_text = r.recognize_google(audio, language="en-US")
print(audio_text)

# List of languages availaible - print(googletrans.LANGUAGES)
# translate to german
translator = Translator()
result = translator.translate(audio_text, dest="de")
print(result.text)

tts = gTTS(result.text,lang="de",slow=True)
tts.save("translation.mp3")

# Play the audio file
os.system("afplay translation.mp3") 
# os.system("start translation.mp3") - for Windows users 