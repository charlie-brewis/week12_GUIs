from tkinter import Tk

win = Tk()

width = 400
height = 400
# x = win.winfo_screenwidth() // 2 - width // 2
# y = win.winfo_screenheight() // 2 - height // 2
x = win.winfo_screenwidth() - width // 2
y = win.winfo_screenheight() - height // 2

win.geometry(f"{width}x{height}+{x}+{y}")
win.mainloop()