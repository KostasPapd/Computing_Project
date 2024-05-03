from tkinter import *
from tkinter import font as tkfont
from registerMenuTemporary import *

def register():
    pass
def createMenu():
    win = Tk()

    win.geometry("500x500")
    win.title("Testing")

    text = tkfont.Font(font="Arial", size=36)
    regButton = Button(text="Register", command=lambda: register(), font=text)
    regButton.grid(row=10, column=10, pady=200, padx=205, sticky="NW")


    win.mainloop()

createMenu()

"""
Make register and login windows
Add subroutines that run the other window programs
Error messages for invalid data
"""