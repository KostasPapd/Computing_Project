from tkinter import *
from PIL import ImageTk, Image

win = Tk()

win.geometry("700x500")

frame = Frame(win, width=60, height=40)
frame.pack()
frame.place(x=10, y=10)

img = Image.open("testLogo.png")
img = img.resize((50, 40))
img = ImageTk.PhotoImage(img)

label = Label(frame, image=img)
label.pack()

win.mainloop()

