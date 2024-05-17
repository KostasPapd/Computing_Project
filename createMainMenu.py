from tkinter import *
from PIL import ImageTk, Image


def register(window):
    import registerMenu
    window.destroy()
    registerMenu.createBox()


def log(window):
    import logInMenu
    window.destroy()
    logInMenu.createLogIn()


def exitMenu(win):
    win.destroy()


def createMenu():
    win = Tk()

    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    win.title("The Physics Lab")

# ADD WHEN LOGO IS DONE
    # frame = Frame(win, width=60, height=40)
    # frame.pack()
    # frame.place(x=90, y=50)

    # img = Image.open("iconNotPng.png")  # LOGO GOES HERE
    # img = img.resize((120, 120))
    # img = ImageTk.PhotoImage(img)

    # label = Label(frame, image=img)
    # label.pack()

    regButton = Button(win, text="Register", command=lambda: register(win))
    regButton.config(font=("Arial", 20))
    regButton.place(relx=0.37, rely=0.4, relheight=0.11, relwidth=0.23)

    logButton = Button(win, text="Log In", command=lambda: log(win))
    logButton.config(font=("Arial", 20))
    logButton.place(relx=0.37, rely=0.55, relheight=0.11, relwidth=0.23)

    exitButton = Button(win, text="Exit", command=lambda: exitMenu(win))
    exitButton.config(font=("Arial", 20))
    exitButton.place(relx=0.37, rely=0.7, relheight=0.11, relwidth=0.23)

    win.mainloop()
