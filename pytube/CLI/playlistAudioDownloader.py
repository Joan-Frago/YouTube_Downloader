from pytube import Playlist
import os

def Download(playlist):
    print("Downloading...")
    for video in playlist.videos:
        audio_stream = video.streams.get_audio_only()
        if audio_stream:
            try:
                audio_stream.download(output_path="../output")
            except Exception as e:
                print(f"Error downloading video: {e}")
        else:
            print(f"No audio-only stream available for video: {video.title}")
    print("Playlist Downloaded Successfully")

def ConfirmDownload(playlist):
    is_download = str(input("\n Are you sure you want to download it? (Y / N): ").lower())
    if is_download == "y":
        Download(playlist)
    elif is_download == "n":
        exit()
    else:
        print("not a correct value, try again")

"""def InfoPlaylist(playlist):
    print(f"\n Title \n {playlist.title} \n\n File Size \n {playlist.filesize / 1000000} MB")
    ConfirmDownload(playlist)"""

def FindPlaylist():
    os.system("clear")
    playlist_url = str(input(("Type in the URL of the playlist you want to download: \n --> ")))
    try:
        playlist = Playlist(playlist_url)
    except:
        print("URL not valid")
        exit()
  
    ConfirmDownload(playlist)
    #InfoPlaylist(playlist)