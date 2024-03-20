from pytube import YouTube

video_url = str(input(("Type in the URL of the video you want to download: \n")))

try:
  video = YouTube(video_url)
  print(f"\n Title \n {video.title}")

  is_download = str(input("\n Are you sure you want to download it? (Y / N): "))
  try:
    if is_download.lower() == "y":
      video.download()
    elif is_download.lower() == "n":
      exit()
  except:
    print("not a correct value, try again")
except:
  print("URL not valid")

