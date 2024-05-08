from tkinter import *
from tkinter import messagebox

def logIn():
    print("Test")

def createLogIn():
    win = Tk()

    win.geometry("500x350")
    win.title("Log In")

    titleLabel = Label(win, text="Log In")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(x=200, y=25)

    logButton = Button(win, text="Log In", command=lambda: logIn())
    logButton.config(font=("Arial", 16))
    logButton.place(x=202, y=275)

    userLabel = Label(win, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(x=82, y=93)
    userBox = Text(win, height=1, width=30)
    userBox.place(x=185, y=100)

    passLabel = Label(win, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(x=85, y=170)
    passBox = Text(win, height=1, width=30)
    passBox.place(x=185, y=175)

    win.mainloop()


# createLogIn()
# REMOVE OR BIG PROBLEMS
