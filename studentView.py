from tkinter import *
from tkinter.tix import *
from createMainMenu import createMenu

# ADD CLASS TO CREATE MENU BAR

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


    win.attributes("-fullscreen", True)
    win.resizable(False, False)
    win.mainloop()
