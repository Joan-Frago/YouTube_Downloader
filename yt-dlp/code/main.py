# import libraries
try:
    import json
    import yt_dlp
    import sys
except Exception as e:
    print(e)

def Select():
    try:
        option = int(input("What do you want to download?\n 1. Audio (single video)\n 2. Video (single video)\n 3. Audio (playlist)\n 4. Video (playlist)\n\n --> "))
        if option not in [1, 2, 3, 4]:
            print("Please choose a valid option")
    except Exception as e:
        print("Please answer with a number")
        return Select()
    return option

def getInfo(aurl:str, aopts:dict, infoFile:str):
    try:
        with yt_dlp.YoutubeDL(aopts) as ydl:
            info = ydl.extract_info(aurl, download=False)

            # ydl.sanitize_info makes the info json-serializable
            info = json.dumps(ydl.sanitize_info(info))
            with open(infoFile, "w") as json_file:
                json_file.write(info)
    except Exception as e:
        print(e)

def downloadMedia(aurl:str, aopts:dict):
    try:
        with yt_dlp.YoutubeDL(aopts) as ydl:
            error_code = ydl.download([aurl])
            print("Some videos failed to download" if error_code else "All videos successfully downloaded")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    option = Select()
    infoFile = "../tmp/info.json"
    iurl = str(input("Paste the URL of the video or playlist you want to download\n\n --> "))

    # Set default options based on user choice
    audio_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'ignoreerrors': True,
        'outtmpl': '../audios/%(title)s.%(ext)s'
    }
    video_opts = {
        'format': 'best',
        'ignoreerrors': True,
        'outtmpl': '../videos/%(title)s.%(ext)s'
    }

    # Download based on the option selected
    if option == 1:  # Audio - Single Video
        downloadMedia(iurl, audio_opts)
    elif option == 2:  # Video - Single Video
        downloadMedia(iurl, video_opts)
    elif option == 3:  # Audio - Playlist
        audio_opts['noplaylist'] = False  # Ensure playlists are downloaded
        downloadMedia(iurl, audio_opts)
    elif option == 4:  # Video - Playlist
        video_opts['noplaylist'] = False  # Ensure playlists are downloaded
        downloadMedia(iurl, video_opts)

    sys.exit()
