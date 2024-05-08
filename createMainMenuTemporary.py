from tkinter import *

def register():
    import registerMenuTemporary
    registerMenuTemporary.createBox()


def createMenu():
    win = Tk()

    win.geometry("500x500")
    win.title("Testing")

    regButton = Button(win, text="Test_Register", command=lambda: register())
    regButton.config(font=("Arial", 20))
    regButton.grid(row=10, column=10, pady=200, padx=205, sticky="NW")


    win.mainloop()

createMenu()

"""
FIX ISSUE WITH EXITING WINDOW - look at old code/consult with abid
Make register and login windows
Add subroutines that run the other window programs
Error messages for invalid data
"""