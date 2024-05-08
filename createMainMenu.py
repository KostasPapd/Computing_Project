from tkinter import *

def register(window):
    import registerMenu
    window.destroy()
    registerMenu.createBox()

def log(window):
    import logInMenu
    window.destroy()
    logInMenu.createLogIn()

def createMenu():
    win = Tk()

    win.geometry("500x500")
    win.title("Testing")

    regButton = Button(win, text="Register", command=lambda: register(win))
    regButton.config(font=("Arial", 20))
    regButton.place(x=180, y=200)

    logButton = Button(win, text="Log In", command=lambda: log(win))
    logButton.config(font=("Arial", 20))
    logButton.place(x=190, y=300)


    win.mainloop()

createMenu()

"""
Make register and login windows
Add subroutines that run the other window programs
Error messages for invalid data
"""