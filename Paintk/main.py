from tkinter import *
import pyscreenshot


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

        self.oval_brush = TRUE
        self.line_brush = FALSE
        self.erase_brush = FALSE

        self.colors = {"black", "gray", "white", "red",
                       "green", "blue", "purple", "orange", "cyan", "cyan2"}
        self.pick_color = "black"
        self.bar_menu = Frame(self.window, bg="#3b3b3b", height=50)
        self.bar_menu.pack(fill="x")

        self.label_color = Label(self.bar_menu, text="Color:  ", fg="white", bg="#3b3b3b")
        self.label_color.pack(side=LEFT)

        for i in self.colors:
            Button(self.bar_menu, bg=i,
                   width=1, height=1, command=lambda col=i: self.select_color(col)).pack(side=LEFT)

        self.tex_pen_size = Label(self.bar_menu, text="  Size:  ", fg="white", bg="#3b3b3b")
        self.tex_pen_size.pack(side=LEFT)
        self.pen_size = Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side=LEFT)
        self.label_brushes = Label(self.bar_menu, text="  Brushes:  ", fg="white", bg="#3b3b3b")
        self.label_brushes.pack(side=LEFT)

        self.btn_line = Button(self.bar_menu, image=self.img_line, bd=0, width=30, height=30, command=self.brush_line)
        self.btn_line.pack(side=LEFT)
        self.btn_oval = Button(self.bar_menu, image=self.img_oval, bd=0, width=30, height=30, command=self.brush_oval)
        self.btn_oval.pack(side=LEFT)
        self.btn_erase = Button(self.bar_menu, image=self.img_erase, bd=0, width=30, height=30, command=self.brush_erase)
        self.btn_erase.pack(side=LEFT)
        self.btn_square = Button(self.bar_menu, image=self.img_square, bd=0, width=30, height=30, command=None)
        self.btn_square.pack(side=LEFT)

        self.label_option = Label(self.bar_menu, text="  Options:  ", fg="white", bg="#3b3b3b")
        self.label_option.pack(side=LEFT)
        self.btn_new = Button(self.bar_menu, image=self.img_new, bd=0, width=30, height=30, command=self.clear)
        self.btn_new.pack(side=LEFT)
        self.btn_save = Button(self.bar_menu, image=self.img_save, bd=0, width=30, height=30, command=None)
        self.btn_save.pack(side=LEFT)

        self.area_draw = Canvas(self.window, bg="gainsboro", height=600)
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)

        self.window.mainloop()

    def select_color(self, col):
        self.pick_color = col

    def draw(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2,
                                       fill=self.pick_color, outline=self.pick_color, width=self.pen_size.get())
        elif self.line_brush:
            self.area_draw.create_line(x1 - 200, y1, x2, y2, fill=self.pick_color, width=self.pen_size.get())
        else:
            self.area_draw.create_oval(x1, y1, x2, y2,
                                       fill="gainsboro", outline="gainsboro", width=self.pen_size.get())

    def brush_oval(self):
        self.oval_brush = TRUE
        self.line_brush = FALSE
        self.erase_brush = FALSE

    def brush_line(self):
        self.oval_brush = FALSE
        self.line_brush = TRUE
        self.erase_brush = FALSE

    def brush_erase(self):
        self.oval_brush = FALSE
        self.line_brush = FALSE
        self.erase_brush = TRUE

    def clear(self):
        self.area_draw.delete("all")


Paintk()