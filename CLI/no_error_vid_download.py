from pytube import YouTube

usr_url = str(input("URL --> "))

video = YouTube(url = usr_url)
video = video.streams.get_highest_resolution()

video.download(output_path="/Users/joanpersonal/Documents/Personal/YTDownloader/Movies")