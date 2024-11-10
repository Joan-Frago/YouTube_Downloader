import tkinter as tk
import audioDownloader
import videoDownloader

window = tk.Tk()
window.title("YouTube Downloader")

def draWindow():
    # Get Screen Dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate coordinates to center window
    WIDTH = 800
    HEIGHT = 450
    x_position = (screen_width - WIDTH) // 2
    y_position = (screen_height - HEIGHT) // 2

    # Establish window position
    window.geometry(f"{WIDTH}x{HEIGHT}+{x_position}+{y_position}")

    # Title
    title = tk.Label(window, text="YouTube Downloader", fg="white", font=("Arial", 40), anchor="center")
    title.pack()

    # YouTube Link
    link = tk.Entry(window, width=300)
    link.pack()

    # Selector
    audDownload = tk.Button(window, text="Download Audio", fg="black", bg="white", font=("Arial", 30), command=audioDownloader.test(link.get()))
    vidDownload = tk.Button(window, text="Download Video", fg="black", bg="white", font=("Arial", 30), command=videoDownloader.test(link.get()))
        
    vidDownload.pack()
    audDownload.pack()

def main():
    draWindow()

    window.mainloop()

if __name__ == "__main__":
    main()