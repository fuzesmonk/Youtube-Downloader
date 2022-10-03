from turtle import title
from pytube import YouTube
import os

def downloader():
    video = input("Enter Video Link: ")
    video = YouTube(video)
    confirmation = input(f"Is this the title of the video you want to download(Y/N)? {video.title}: ") 
    if confirmation == "Y":
        audioonly = input("Do you want to only download the audio from the video: ")
        if audioonly == "Y" or "y": 
            print(video.streams.filter(only_audio=True, file_extension ='mp4'))
        else:
            typeofvideo = input("Do you want video and audio tracks on one file?(This can cause lower quality for both audio and video): ")
            if typeofvideo == "Y":
                print(video.streams.filter(progressive=True))
            else:
                print(video.streams.filter(adaptive=True))
    videostreamchoice = input("Enter the itag number for the quality you want to download the video in: ")
    videodownload = video.streams.get_by_itag(videostreamchoice)
    videodownload.download()
downloader()

    


