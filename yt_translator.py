# from pytube import YouTube
# from googletrans import Translator
# import ssl
# import urllib.request


# # url = input("Enter the YouTube video URL: ")

# yt = YouTube("https://youtu.be/_4hVYXTz3Bk")
# stream = yt.streams.get_highest_resolution()
# stream.download()

# translator = Translator()
# captions = yt.captions["en"]
# captions_text = captions.generate_srt_captions()
# translated_captions = translator.translate(captions_text, dest='de').text

# with open('translated_captions.txt', 'w', encoding='utf-8') as f:
#     f.write(translated_captions)

from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = "https://youtu.be/_4hVYXTz3Bk"
Download(link)