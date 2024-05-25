from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

window = ThemedTk(theme="blue")
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()