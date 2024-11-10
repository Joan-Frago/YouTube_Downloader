# Video example --> https://youtu.be/SICEtxAc1i4?si=Dxiqp3KxI-vVZvL6
# Playlist example --> https://www.youtube.com/playlist?list=PLthLmPLEszwHBOQab2_jvY9_fbvaBBopJ

import audioDownloader
import videoDownloader
import playlistVideoDownloader
import playlistAudioDownloader
import os
os.system("clear")

def select():
    option = int(input("\n 1.    Download Video\n 2.    Download Audio\n 3.    Download Video Playlist\n 4.    Download Audio Playlist\n\n --> "))
    if option == 1:
        # call Download Video function
        videoDownloader.FindVideo()
    elif option == 2:
        #call Download Audio function
        audioDownloader.FindVideo()
    elif option == 3:
        playlistVideoDownloader.FindPlaylist()
    elif option == 4:
        playlistAudioDownloader.FindPlaylist()
    else:
        print("Not an option")
        select()

if __name__ == "__main__":
    select()