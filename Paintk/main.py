from tkinter import *


class Paintk:

    def __init__(self):
        self.window = Tk()
        self.window.title("Paint TK")
        self.window.minsize(width=1200, height=600)
        self.window.resizable(0, 0)

        self.img_erase = PhotoImage(file="icons/eraser.png")
        self.img_line = PhotoImage(file="icons/line.png")
        self.img_oval = PhotoImage(file="icons/oval.png")
        self.img_new = PhotoImage(file="icons/new.png")
        self.img_save = PhotoImage(file="icons/save.png")
        self.img_square = PhotoImage(file="icons/square.png")

        self.colors = {"black", "gray", "white", "red",
                       "green", "blue", "purple", "orange"}
        self.bar_menu = Frame(self.window, bg="#3b3b3b", height=50)
        self.bar_menu.pack(fill="x")

        self.label_color = Label(self.bar_menu, text="Color:  ", fg="white", bg="#3b3b3b")
        self.label_color.pack(side=LEFT)

        for i in self.colors:
            Button(self.bar_menu, bg=i,
                   width=1, height=1, command=None).pack(side=LEFT)

        self.label_brushes = Label(self.bar_menu, text="Brushes:  ", fg="white", bg="#3b3b3b")
        self.label_brushes.pack(side=LEFT)

        #self.btn_new = Button(self.bar_menu, image=self.img_new, width=30, height=30, command=None)
        #self.btn_new.pack(side=LEFT)
        self.btn_line = Button(self.bar_menu, image=self.img_line, width=30, height=30, command=None)
        self.btn_line.pack(side=LEFT)
        self.btn_oval = Button(self.bar_menu, image=self.img_oval, width=30, height=30, command=None)
        self.btn_oval.pack(side=LEFT)
        self.btn_square = Button(self.bar_menu, image=self.img_square, width=30, height=30, command=None)
        self.btn_square.pack(side=LEFT)
        #self.btn_erase = Button(self.bar_menu, image=self.img_erase, width=30, height=30, command=None)
        #self.btn_erase.pack(side=LEFT)

        self.area_draw = Canvas(self.window, bg="white", height=600)
        self.area_draw.pack(fill="both")

        self.window.mainloop()


Paintk()
