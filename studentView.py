from tkinter import *


def exitView(win):
    win.destroy()


def createStudent():
    win = Tk()

    win.title("Student View")
    win.geometry("500x500")

    nameText = "Name test"
    testLabel = Label(win, text=nameText, font="Arial 60 bold")
    testLabel.place(relx=0.15, rely=0.05, relheight=0.1, relwidth=0.7)

    exitButton = Button(win, text="Exit", command=lambda: exitView(win))
    exitButton.config(font=("Arial", 20))
    exitButton.place(relx=0.4, rely=0.7, relheight=0.11, relwidth=0.23)

    win.attributes("-fullscreen", True)
    win.resizable(False, False)
    win.mainloop()
