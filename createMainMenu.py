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

    win.geometry("500x500")
    win.title("The Physics Lab")

    frame = Frame(win, width=60, height=40)
    frame.pack()
    frame.place(x=90, y=50)

    img = Image.open("testLogo2png.png")
    img = img.resize((300, 120))
    img = ImageTk.PhotoImage(img)

    label = Label(frame, image=img)
    label.pack()

    regButton = Button(win, text="Register", command=lambda: register(win))
    regButton.config(font=("Arial", 20))
    regButton.place(x=180, y=200)

    logButton = Button(win, text="Log In", command=lambda: log(win))
    logButton.config(font=("Arial", 20))
    logButton.place(x=190, y=275)

    exitButton = Button(win, text="Exit", command=lambda: exitMenu(win))
    exitButton.config(font=("Arial", 20))
    exitButton.place(x=200, y=350)

    win.mainloop()
