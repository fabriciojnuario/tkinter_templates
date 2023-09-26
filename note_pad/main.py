import tkinter
import tkinter as tk


def new_file():
    text_area.delete(1.0, "end")
    print("Create new file\n")


def save_file():
    container = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()
    print("Save file\n")


def open_file():
    file = open("notepad.txt", "r")
    container = file.read()
    text_area.insert(1.0, container)
    print("Save as file\n")


def apply_update():
    type = spin_font_type.get()
    size = spin_font_size.get()
    text_area.config(font="{} {}".format(type, size))


root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

frame = tk.Frame(root, height=30)
frame.pack(fill="x")

font_text = tk.Label(frame, text=" Font: ")
font_text.pack(side="left")

spin_font_type = tk.Spinbox(frame, values=("Arial", "Verdana"))
spin_font_type.pack(side="left")

font_size = tk.Label(frame, text=" Font size: ")
font_size.pack(side="left")

spin_font_size = tk.Spinbox(frame, from_=0, to=60)
spin_font_size.pack(side="left")

button_update = tk.Button(frame, text="apply", command=apply_update)
button_update.pack(side="left")

text_area = tk.Text(root, font="Arial 13 bold", width=800, height=600)
text_area.pack(expand=1)

main_menu = tk.Menu(root)

file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)
main_menu.add_cascade(label="File", menu=file_menu)

root.config(menu=main_menu)

root.mainloop()
