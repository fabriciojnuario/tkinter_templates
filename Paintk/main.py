from tkinter import *


class Paintk:

    def __init__(self):
        self.window = Tk()
        self.window.title("Paint TK")
        self.window.minsize(width=1200, height=600)
        self.window.resizable(0, 0)
        self.bar_menu = Frame(self.window, bg="#3b3b3b", height=50)
        self.bar_menu.pack(fill="x")

        self.label_color = Label(self.bar_menu, text="Color:  ", fg="white", bg="#3b3b3b")
        self.label_color.pack(side=LEFT)
        self.button_color = Button(self.bar_menu, bg="black", width=1, height=1, command=None)
        self.button_color.pack(side=LEFT)

        self.area_draw = Canvas(self.window, bg="white", height=600)
        self.area_draw.pack(fill="both")

        self.window.mainloop()


Paintk()
