from pytube import YouTube
from pytube.cli import on_progress
import ssl
import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 150
WINDOW_TITLE = "Youtube downloader"



class YoutubeDownloader:

    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.configure(bg="#a991c3")
        self.window.title(WINDOW_TITLE)

                                     # labels

        self.link_label = tk.Label(self.window, text="Download Link")
        self.link_label.grid(column=0, row=0)
        self.name_label = tk.Label(self.window, text="Save File as")
        self.name_label.grid(column=0, row=1)
        self.path_label = tk.Label(self.window, text="Save File Path")
        self.path_label.grid(column=0, row=2)
        self.ext_label = tk.Label(self.window, text="File extension")
        self.ext_label.grid(column=0, row=3)
        self.my_name = tk.Label(self.window,  text = 'Developed by: Cheikhouna Mbacke', bg = 'black', fg = 'white')
        self.my_name.grid(column = 0, row = 6)


        # entry

        self.link_entry = tk.Entry(master=self.window, width=40)
        self.link_entry.grid(column=1, row=0)
        self.name_entry = tk.Entry(master=self.window, width=40)
        self.name_entry.grid(column=1, row=1)
        self.path_entry = tk.Entry(master=self.window, width=40)
        self.path_entry.grid(column=1, row=2)
        self.ext_entry = tk.Entry(master=self.window, width=40)
        self.ext_entry.grid(column=1, row=3)
        self.download_button = tk.Button(self.window, text="Download", command=self.__get_link)
        self.download_button.grid(column=1, row=4)

        return

                                    # function to download video

    def __downloader(self, link, save_path="", save_name="", extension="mp4"):
        yt = YouTube(link)
        yt_stream = yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first()
        yt_stream.download(output_path=save_path, filename=save_name)

        return


    def __get_link(self):
        link = self.link_entry.get()
        path = self.path_entry.get()
        name = self.name_entry.get()
        ext = self.ext_entry.get()

        self.__downloader(link, path, name, ext)

        return





    def run_app(self):
        self.window.mainloop()
        return


if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run_app()