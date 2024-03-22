# https://youtu.be/SICEtxAc1i4?si=Dxiqp3KxI-vVZvL6

import audioDownloader
import videoDownloader
import os
os.system("clear")

def select():
    try:
        option = int(input("\n 1.    Download Video\n 2.    Download Audio\n\n --> "))
        if option == 1:
            # call Download Video function
            videoDownloader.FindVideo()
        elif option == 2:
            #call Download Audio function
            audioDownloader.FindVideo()
        else:
            print("Not an option")
    except:
        print("Type a number")
        select()

select()