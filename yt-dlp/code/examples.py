# Example URL https://www.youtube.com/watch?v=9m4aZGHFBik
# Example URL of playlist https://www.youtube.com/playlist?list=PLx3GB9osG9QTMdnMt-4b1_1MOHzI-NoWF

# ------------- EXTRACTING INFORMATION ----------------
import json
import yt_dlp

URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'

# See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))


# ------------- DOWNLOAD USING AN info-json -------------
import yt_dlp

INFO_FILE = 'path/to/video.info.json'

with yt_dlp.YoutubeDL() as ydl:
    error_code = ydl.download_with_info_file(INFO_FILE)

print('Some videos failed to download' if error_code
      else 'All videos successfully downloaded')



# -------------- EXTRACT AUDIO ---------------------------
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)