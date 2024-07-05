import tkinter
from tkinter import *
import SQLfunctions

def createAssign(tName):
    win = Toplevel()
    win.title("Create Assignment")

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleL = Label(win, text="Create Assignment", font=("Arial", 20))
    titleL.place(relx=0.25, rely=0.05, relheight=0.13, relwidth=0.5)

    assignName = Label(win, text="Assignment Title:", font=("Arial", 16))
    assignName.place(relx=0.03, rely=0.25, relheight=0.13, relwidth=0.4)

    nameVar = tkinter.StringVar()
    nameEntry = Entry(win, textvariable=nameVar, font=('Arial', 12), width=27)
    nameEntry.place(relx=0.4, rely=0.28, relheight=0.07, relwidth=0.5)

    classLabel = Label(win, text="Class:", font=("Arial", 16))
    classLabel.place(relx=0.225, rely=0.45, relheight=0.13, relwidth=0.2)

    # classes = SQLfunctions.getClass(tName)
    classes = ["Class 1", "Class 2", "Class 3"]
    clicked = StringVar()
    clicked.set("Class")
    classMenu = OptionMenu(win, clicked, *classes)
    classMenu.place(relx=0.4, rely=0.46, relheight=0.1, relwidth=0.25)

    nextButton = Button(win, text="Next", font=("Arial", 16), command=lambda: SQLfunctions.createAssign(nameVar.get()
                                                                                                        , tName, win))
    nextButton.place(relx=0.6, rely=0.7, relheight=0.13, relwidth=0.2)

    cancelButton = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelButton.place(relx=0.2, rely=0.7, relheight=0.13, relwidth=0.2)

    win.resizable(False, False)
    win.mainloop()

def nextAssign(name, tName, win):
    win.destroy()
    createQs(name, tName)

def createQs(name, tName):
    win = Toplevel()
    win.title("Create Question")


if __name__ == "__main__":
    createAssign("Kostas Papadopoulos")
    pass
