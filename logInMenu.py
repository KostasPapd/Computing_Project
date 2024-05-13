import tkinter
from tkinter import *
from tkinter import messagebox

def logIn(username, password):
    username = username.get("1.0", "end-1c").strip()  # Pass these value to check against the database
    password = password.get().strip()  # Maybe different file

def back(win):
    import createMainMenu
    win.destroy()
    createMainMenu.createMenu()

def createLogIn():
    win = Tk()

    win.geometry("500x350")
    win.title("Log In")

    password_variable = tkinter.StringVar()

    titleLabel = Label(win, text="Log In")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(x=200, y=25)

    backButton = Button(win, text="Back", command=lambda: back(win))
    backButton.config(font=("Arial", 16))
    backButton.place(x=275, y=275)

    logButton = Button(win, text="Log In", command=lambda: logIn(userBox, passBox))
    logButton.config(font=("Arial", 16))
    logButton.place(x=150, y=275)

    userLabel = Label(win, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(x=82, y=93)
    userBox = Text(win, height=1, width=30)
    userBox.place(x=185, y=100)

    passLabel = Label(win, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(x=85, y=170)
    passBox = Entry(win, textvariable=password_variable, font=('Arial', 12), show='• ', width=27)
    passBox.place(x=185, y=175)

    win.mainloop()
