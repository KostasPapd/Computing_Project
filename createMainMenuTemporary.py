from tkinter import *
from tkinter import font as tkfont
import registerMenuTemporary

def register():
    registerMenuTemporary.createBox()
def createMenu():
    win = Tk()

    win.geometry("500x500")
    win.title("Testing")

    text = tkfont.Font(font="Arial", size=36)
    regButton = Button(win, text="Register", command=lambda: register(), font=text)
    regButton.grid(row=10, column=10, pady=200, padx=205, sticky="NW")


    win.mainloop()

createMenu()

"""
FIX ISSUE WITH REGISTER WINDOW - look at old code/consult with abid
Make register and login windows
Add subroutines that run the other window programs
Error messages for invalid data
"""