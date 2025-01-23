import tkinter
from tkinter import *
import SQLfunctions
from PIL import Image, ImageTk
from tkinter import messagebox


def logIn(username, password, win):
    usernameVal = username.get("1.0", "end-1c").strip()  # Pass these value to check against the database
    passwordVal = password.get().strip()
    check = SQLfunctions.checkLogIn(usernameVal.lower(), passwordVal) # Check if the login is correct
    if check is None:
        messagebox.showwarning("Incorrect Login", "Incorrect username or password")
    else:
        from twoFactorAuth import createWindow
        createWindow(check, win)

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

    win.title("The Physics Lab - Log In")

    password_variable = tkinter.StringVar()

    frame = Frame(win, width=1, height=1)
    frame.pack()
    frame.place(relx=0.5, rely=0.175, anchor="center")

    img = Image.open("Pictures\\logo.png")
    img = img.resize((int(img.width * 0.3), int(img.height * 0.3)))
    img = ImageTk.PhotoImage(img)

    label = Label(frame, image=img)
    label.pack()

    titleLabel = Label(win, text="Log In")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(relx=0.15, rely=0.275, relheight=0.1, relwidth=0.7)

    exitButton = Button(win, text="Exit", command=lambda: win.destroy())
    exitButton.config(font=("Arial", 16))
    exitButton.place(relx=0.55, rely=0.8, relheight=0.13, relwidth=0.15)

    def enter(event=None):
        logIn(userBox, passBox, win)

    logButton = Button(win, text="Log In", command=enter)
    logButton.config(font=("Arial", 16))
    logButton.place(relx=0.28, rely=0.8, relheight=0.13, relwidth=0.2)

    userLabel = Label(win, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(relx=0.12, rely=0.4, relheight=0.13, relwidth=0.2)
    userBox = Text(win, height=1, width=30)
    userBox.place(relx=0.34, rely=0.44, relheight=0.06, relwidth=0.48)

    passLabel = Label(win, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(relx=0.12, rely=0.6, relheight=0.13, relwidth=0.2)
    passBox = Entry(win, textvariable=password_variable, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.34, rely=0.64, relheight=0.06, relwidth=0.48)

    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(win, image=showPassImg, borderwidth=0, command=lambda: togglePass(passBox))
    showPass.place(relx=0.85, rely=0.63, relheight=0.07, relwidth=0.1)

    win.bind("<Return>", enter)

    userBox.focus()
    win.resizable(False, False)
    win.mainloop()

if __name__ == "__main__":
    # Testing
    createLogIn()
    pass
