import tkinter as tk
from tkinter import ttk


class Calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.resizable(0, 0)

        self.screen_number = tk.Entry(self.window, font='arial 20 bold', justify=tk.RIGHT)
        self.screen_number.pack()

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.button_1 = tk.Button(self.frame, bg='orange', bd=0, text='1', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('1'))
        self.button_1.grid(row=0, column=0)

        self.button_2 = tk.Button(self.frame, bg='orange', bd=0, text='2', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('2'))
        self.button_2.grid(row=0, column=1)

        self.button_3 = tk.Button(self.frame, bg='orange', bd=0, text='3', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('3'))
        self.button_3.grid(row=0, column=2)

        self.button_4 = tk.Button(self.frame, bg='orange', bd=0, text='4', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('4'))
        self.button_4.grid(row=1, column=0)

        self.button_5 = tk.Button(self.frame, bg='orange', bd=0, text='5', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('5'))
        self.button_5.grid(row=1, column=1)

        self.button_6 = tk.Button(self.frame, bg='orange', bd=0, text='6', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('6'))
        self.button_6.grid(row=1, column=2)

        self.button_7 = tk.Button(self.frame, bg='orange', bd=0, text='7', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('7'))
        self.button_7.grid(row=2, column=0)

        self.button_8 = tk.Button(self.frame, bg='orange', bd=0, text='8', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('8'))
        self.button_8.grid(row=2, column=1)

        self.button_9 = tk.Button(self.frame, bg='orange', bd=0, text='9', fg='white',
                                  font='arial 20 bold', width=3, height=1, command=lambda: self.touch('9'))
        self.button_9.grid(row=2, column=2)

        self.button_add = tk.Button(self.frame, bg='orange', bd=0, text='+', fg='white',
                                    font='arial 20 bold', width=3, height=1, command=lambda: self.touch('+'))
        self.button_add.grid(row=0, column=3)

        self.button_sub = tk.Button(self.frame, bg='orange', bd=0, text='-', fg='white',
                                    font='arial 20 bold', width=3, height=1, command=lambda: self.touch('-'))
        self.button_sub.grid(row=1, column=3)

        self.button_mult = tk.Button(self.frame, bg='orange', bd=0, text='x', fg='white',
                                     font='arial 20 bold', width=3, height=1, command=lambda: self.touch('*'))
        self.button_mult.grid(row=2, column=3)

        self.button_div = tk.Button(self.frame, bg='orange', bd=0, text='/', fg='white',
                                    font='arial 20 bold', width=3, height=1, command=lambda: self.touch('/'))
        self.button_div.grid(row=3, column=3)

        self.button_equal = tk.Button(self.frame, bg='orange', bd=0, text='=', fg='white',
                                      font='arial 20 bold', width=3, height=1, command=self.total)
        self.button_equal.grid(row=3, column=2)

        self.button_clear = tk.Button(self.frame, bg='orange', bd=0, text='C', fg='white',
                                      font='arial 20 bold', width=3, height=1, command=self.clean)
        self.button_clear.grid(row=3, column=0)

        self.button_point = tk.Button(self.frame, bg='orange', bd=0, text='.', fg='white',
                                      font='arial 20 bold', width=3, height=1, command=lambda: self.touch('.'))
        self.button_point.grid(row=3, column=1)

        self.window.mainloop()

    def touch(self, num):
        self.screen_number.insert(tk.END, num)

    def clean(self):
        self.screen_number.delete(0, tk.END)

    def total(self):
        total = eval(self.screen_number.get())
        self.clean()
        self.screen_number.insert(0, str(total))


Calc()
