import tkinter
from tkinter import *
from tkinter import messagebox  # For wrong username/password pop-ups


def logIn(username, password):
    username = username.get("1.0", "end-1c").strip()  # Pass these value to check against the database
    password = password.get().strip()  # Maybe different file


def back(win):
    import createMainMenu
    win.destroy()
    createMainMenu.createMenu()


def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")


def createLogIn():
    win = Tk()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Log In")

    password_variable = tkinter.StringVar()

    titleLabel = Label(win, text="Log In")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(relx=0.13, rely=0.05, relheight=0.1, relwidth=0.7)

    backButton = Button(win, text="Back", command=lambda: back(win))
    backButton.config(font=("Arial", 16))
    backButton.place(relx=0.55, rely=0.8, relheight=0.13, relwidth=0.15)

    logButton = Button(win, text="Log In", command=lambda: logIn(userBox, passBox))
    logButton.config(font=("Arial", 16))
    logButton.place(relx=0.28, rely=0.8, relheight=0.13, relwidth=0.2)

    userLabel = Label(win, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(relx=0.15, rely=0.24, relheight=0.13, relwidth=0.2)
    userBox = Text(win, height=1, width=30)
    userBox.place(relx=0.37, rely=0.28, relheight=0.06, relwidth=0.48)

    passLabel = Label(win, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(relx=0.15, rely=0.5, relheight=0.13, relwidth=0.2)
    passBox = Entry(win, textvariable=password_variable, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.37, rely=0.54, relheight=0.06, relwidth=0.48)

    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(win, image=showPassImg, command=lambda: togglePass(passBox))
    showPass.place(relx=0.87, rely=0.53, relheight=0.07, relwidth=0.1)

    userBox.focus()
    win.mainloop()

createLogIn()