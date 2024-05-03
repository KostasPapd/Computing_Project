from tkinter import *
from tkinter import font as tkfont
import isValid

def createBox():
    win = Tk()

    win.geometry("400x300")
    win.title("Register Account")

    text = tkfont.Font(font="Arial", size=36)
    regButton = Button(text="Register", font=text)
    regButton.grid(row=10, column=10, pady=200, padx=154, sticky="NW")

    win.mainloop()

createBox()

"""
Add text boxes with titles
Run commands that verify data entered
"""