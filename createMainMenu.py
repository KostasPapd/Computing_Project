from tkinter import *

def register():
    import registerMenu
    registerMenu.createBox()

def createMenu():
    win = Tk()

    win.geometry("500x500")
    win.title("Testing")

    regButton = Button(win, text="Test_Register", command=lambda: register())
    regButton.config(font=("Arial", 20))
    regButton.grid(row=10, column=10, pady=200, padx=150, sticky="W")


    win.mainloop()

createMenu()

"""
Make register and login windows
Add subroutines that run the other window programs
Error messages for invalid data
"""