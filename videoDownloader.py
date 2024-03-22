from pytube import YouTube
import os

def Download(video):
  print("Downloading...")
  video.download()
  print("Video Downloaded Successfully")

def ConfirmDownload(video):
  is_download = str(input("\n Are you sure you want to download it? (Y / N): ").lower())
  if is_download == "y":
    Download(video)
  elif is_download == "n":
    exit()
  else:
    print("not a correct value, try again")

def InfoVideo(video):
  print(f"\n Title \n {video.title} \n\n File Size \n {video.filesize / 1000000} MB")
  ConfirmDownload(video)

def FindVideo():
  os.system("clear")
  video_url = str(input(("Type in the URL of the video you want to download: \n --> ")))
  try:
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()
  except:
    print("URL not valid")
    exit()
  
  InfoVideo(video)
