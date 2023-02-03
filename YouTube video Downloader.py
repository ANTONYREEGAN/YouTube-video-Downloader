import pytube
from pytube import YouTube
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been error while downloading")
    print("Download is completed")
link = input("put your youtube video link here: ")
Download(link)