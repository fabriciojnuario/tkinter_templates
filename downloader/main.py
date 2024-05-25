from tkinter import *
#from pytube import YouTube
from tkinter import filedialog
import youtube_dl
import os


class Downloader:

    def __init__(self):
        self.win = Tk()
        self.win.title("Downloader")
        self.win.resizable(0, 0)
        self.win.geometry("850x500+300+200")

        self.img_logo = PhotoImage(file="assets/logo.png")
        self.audio = FALSE
        self.video = FALSE
        self.frame = Frame(self.win, bg="#3b3b3b", pady=60)
        self.frame.pack(fill="x")

        self.label_logo = Label(self.frame, image=self.img_logo, bg="#3b3b3b")
        self.label_logo.pack()

        self.frame2 = Frame(self.win, pady=10)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text=" Insert link: ", font="arial 12")
        self.label_insert.pack(side=LEFT)

        self.link = Entry(self.frame2, width=60)
        self.link.pack(side=LEFT)
        self.play = Button(self.frame2, bg="red", bd=0, text=">", fg="white", width=3, height=1,
                           command=lambda: self.download(self.link.get()))
        self.play.pack(side=LEFT)
        self.ab = lambda: self.download(self.link.get())
        print(self.ab)

        self.frame3 = Frame(self.win)
        self.frame3.pack()

        self.radio1 = Radiobutton(self.frame3, text="Audio", value=0, command=self.validator_audio)
        self.radio1.pack(side=LEFT)
        self.radio2 = Radiobutton(self.frame3, text="Video", value=1, command=self.validator_video)
        self.radio2.pack(side=LEFT)
        self.radio3 = Radiobutton(self.frame3, text="Audio/Video", value=2, command=self.validator_all)
        self.radio3.pack(side=LEFT)

        self.win.mainloop()

    def validator_audio(self):
        self.audio = TRUE
        self.video = FALSE

    def validator_video(self):
        self.audio = FALSE
        self.video = TRUE

    def validator_all(self):
        self.audio = FALSE
        self.video = FALSE

    def download(self, link):
        os.system("youtube_dl" + str(link))
        self.complete()

    def mns(self):
        window = Toplevel()
        window.title("E R R O")
        window.resizable(0, 0)
        window.geometry("300x200")

        text = Label(window, text="Esse link não é válido", font="arial 20 bold", pady=30)
        text.pack()

        button_exit = Button(window, text="OK", bg="lightblue", command=window.destroy)
        button_exit.pack()

    def complete(self):
        window = Toplevel()
        window.title("COMPLETED")
        window.resizable(0, 0)
        window.geometry("300x200")

        text = Label(window, text="Download Efetuado", font="arial 20 bold", pady=30)
        text.pack()

        button_exit = Button(window, text="OK", bg="lightblue", command=window.destroy)
        button_exit.pack()


Downloader()
