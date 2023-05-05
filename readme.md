# Speech Translation Tool
<img align="left" alt="python" width="50px" style="padding-right:10px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" />


This is a Python script that allows you to translate spoken English phrases to German. The script uses the Google Speech Recognition API to transcribe the spoken phrase, then uses the Google Translate API to translate it to German. The translated text is then converted to speech using the Google Text-to-Speech API and played back to the user.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/Thabish-Kader/speech-translation-tool`

2. Install the required Python packages by running `pip install -r requirements.txt` in the project directory.

## Note

1. You might encounter an error while installing portaudio if you are in mac. To solve the error run `brew install portaudio`
2. Make sure to install `pip install googletrans==3.1.0a0` version if you use googletrans==3.0.0 you might get an error `AttributeError: 'NoneType' object has no attribute 'group'`

## Useful Resources

-   [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
-   [List of languages in SpeechRecognition](https://buildmedia.readthedocs.org/media/pdf/py-googletrans/latest/py-googletrans.pdf)
-   [GoogleTrans Alpha version](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group)
