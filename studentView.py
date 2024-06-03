from tkinter import *
from tkinter.tix import *
from createMainMenu import createMenu


def signOut(win):
    win.destroy()
    createMenu()


def exitView(win):
    win.destroy()


def createStudent(name):
    win = Tk()

    win.title("Student View")
    win.geometry("500x500")

    nameText = name
    testLabel = Label(win, text=nameText, font="Arial 60 bold")
    testLabel.place(relx=0.15, rely=0.05, relheight=0.1, relwidth=0.7)

    exitButtonImg = PhotoImage(file="Pictures/exit.png")
    exitButtonImg = exitButtonImg.subsample(15, 15)
    exitButton = Button(win, image=exitButtonImg,  borderwidth=0, command=lambda: exitView(win))
    exitButton.place(relx=0.95, rely=0.01, relheight=0.06, relwidth=0.05)

    signOutImg = PhotoImage(file="Pictures/signOut.png")
    signOutImg = signOutImg.subsample(15, 15)
    signOutButton = Button(win, image=signOutImg, borderwidth=0, command=lambda: signOut(win))
    signOutButton.place(relx=0.89, rely=0.01, relheight=0.06, relwidth=0.05)

    win.attributes("-fullscreen", True)
    win.resizable(False, False)
    win.mainloop()
