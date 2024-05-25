from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import os
import pygame


class Player:
    def __init__(self):
        pygame.mixer.init()

        self.win = ThemedTk(themebg=TRUE, theme="black")
        self.win.configure(bg="black")
        self.win.title("Music Player")
        self.win.resizable(0, 0)
        self.win.geometry("300x400+800+300")

        self.img_add = PhotoImage(file="assets/add.png")
        self.img_forward = PhotoImage(file="assets/next.png")
        self.img_pause = PhotoImage(file="assets/next.png")
        self.img_play = PhotoImage(file="assets/play.png")
        self.img_reward = PhotoImage(file="assets/previus.png")
        self.img_remove = PhotoImage(file="assets/remove.png")

        self.status = 0
        self.local = " "

        self.list = Listbox(self.win, bg="#444444", height=10, fg="gray", selectbackground="blue")
        self.list.pack(fill=X, padx=10, pady=10)

        self.frame = ttk.Frame(self.win)
        self.frame.pack(pady=10)

        self.remove_button = ttk.Button(self.frame, image=self.img_remove, command=self.delete_music)
        self.remove_button.grid(row=0, column=0)

        self.add_button = ttk.Button(self.frame, image=self.img_add, command=self.select_music)
        self.add_button.grid(row=0, column=1)

        self.frame2 = ttk.Frame(self.win)
        self.frame2.pack(pady=10)

        self.reward_button = ttk.Button(self.frame2, image=self.img_reward, command=self.previus_music)
        self.reward_button.grid(row=0, column=0)

        self.play_button = ttk.Button(self.frame2, image=self.img_play, command=self.play_music)
        self.play_button.grid(row=0, column=1)

        self.forward_button = ttk.Button(self.frame2, image=self.img_forward, command=self.next_music)
        self.forward_button.grid(row=0, column=2)

        self.volume = ttk.Scale(self.win, from_=0, to=100,  command=self.volume_set)
        self.volume.pack(fill=X, pady=5, padx=10)

        self.win.mainloop()

    def select_music(self):
        self.local = filedialog.askdirectory()
        print(self.local)
        files = os.listdir(self.local)

        for file in files:
            self.list.insert(END, str(file))

    def delete_music(self):
        self.list.delete(ANCHOR)

    def next_music(self):
        try:
            index = self.list.curselection()[0] + 1
            self.list.selection_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.error_window("This operation can't be done.")

    def previus_music(self):
        try:
            index = self.list.curselection()[0] - 1
            self.list.selection_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.error_window("This operation can't be done.")

    def play_music(self):
        try:
            if self.status == 0:
                pygame.mixer.music.load(str(self.local) + "/" + str(self.list.get(ANCHOR)))
                pygame.mixer.music.play()
                self.play_button.config(image=self.img_pause)
                self.status = 1
            else:
                pygame.mixer.music.pause()
                self.play_button.config(image=self.img_play)
                self.status = 0
        except:
            self.error_window("Not music avaliable.")

    def error_window(self, message):
        window = Toplevel()
        window.title("Error")
        window.resizable(0, 0)
        window.geometry("250x250+300+300")
        window.configure(bg="black")
        lb_warning = ttk.Label(window, text=str(message), background="black")
        lb_warning.pack(expand=YES)

        btn = ttk.Button(window, text="       OK", command=window.destroy)
        btn.pack(pady=15)

    def volume_set(self, var):
        pygame.mixer.music.set_volume(self.volume.get())

Player()
