import os
import sys
import subprocess
import pkg_resources
needed_packages = 'pytube'
class packagecheck:    
    def package_check(): 
        required = {needed_packages}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed 

        if missing:
             python = sys.executable
             subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
packagecheck.package_check()


from pytube import YouTube
class ytdl :
    def downloader():
        video = input("Enter Video Link: ")
        video = YouTube(video)
        confirmation = input(f"Is this the title of the video you want to download(Y/N)? {video.title}: ") 
        if confirmation == "Y":
            videotitle = video.title
            audioonly = input("Do you want to only download the audio from the video: ")
            if audioonly == "Y" or "y": 
                print(video.streams.filter(only_audio=True, file_extension ='mp4'))
                filetype = 'mp4'
            else:
                typeofvideo = input("Do you want video and audio tracks on one file?(This can cause lower quality for both audio and video): ")
                if typeofvideo == "Y":
                    print(video.streams.filter(progressive=True))
                else:
                    print(video.streams.filter(adaptive=True))
        videostreamchoice = input("Enter the itag number for the quality you want to download the video in: ")
        videodownload = video.streams.get_by_itag(videostreamchoice)
        videodownload.download()
        
ytdl.downloader()