import tkinter
from tkinter import *
from tkinter import filedialog
from tkcalendar import Calendar
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
    classLabel.place(relx=0.225, rely=0.4, relheight=0.13, relwidth=0.2)

    # classes = SQLfunctions.getClass(tName)

    classes = ["Class 1", "Class 2", "Class 3"]
    clicked = StringVar()
    clicked.set("Class")
    classMenu = OptionMenu(win, clicked, *classes)
    classMenu.place(relx=0.4, rely=0.41, relheight=0.1, relwidth=0.25)

    def calendar():
        top = Toplevel(win)
        top.title("Choose Date")
        cal = Calendar(top, selectmode='day', year=2024, month=1, day=1)
        cal.pack(pady=20)

        def get_date():
            date = cal.selection_get()
            top.destroy()

        select = Button(top, text="Select", font=("Arial", 14), command=get_date)
        select.pack()

    dueLabel = Label(win, text="Due:", font=("Arial", 16))
    dueLabel.place(relx=0.26, rely=0.55, relheight=0.1, relwidth=0.15)

    dueButton = Button(win, text="Choose Date", font=("Arial", 10), command=lambda: calendar())
    dueButton.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.25)

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

    wWidth = 650
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleLabel = Label(win, text="Add Question", font=("Arial", 20))
    titleLabel.place(relx=0.25, rely=0.01, relheight=0.13, relwidth=0.5)

    questionLabel = Label(win, text="Question:", font=("Arial", 16))
    questionLabel.place(relx=0.05, rely=0.12, relheight=0.05, relwidth=0.15)

    quest = StringVar()
    questionEntry = Entry(win, textvariable=quest, font=('Arial', 12))
    questionEntry.place(relx=0.23, rely=0.12, relheight=0.06, relwidth=0.7)

    marksLabel = Label(win, text="Marks:", font=("Arial", 16))
    marksLabel.place(relx=0.06, rely=0.22, relheight=0.05, relwidth=0.15)

    marksEntry = Text(win, font=("Arial", 16))
    marksEntry.place(relx=0.23, rely=0.22, relheight=0.06, relwidth=0.1)

    answerLabel = Label(win, text="Answer:", font=("Arial", 16))
    answerLabel.place(relx=0.05, rely=0.32, relheight=0.05, relwidth=0.15)

    # CHANGE SO THE WRITING STARTS AT THE TOP AND IT GOES TO THE NEXT LINE WHEN IT REACHES THE END
    answerEntry = Text(win, font=('Arial', 10))
    answerEntry.place(relx=0.23, rely=0.32, relheight=0.5, relwidth=0.7)

    def open_file_dialog():
        filename = filedialog.askopenfilename()

    addFileButton = Button(win, text="Add File", font=("Arial", 16), command=lambda: open_file_dialog())
    # addFileButton.place(relx=0.05, rely=0.4, relheight=0.1, relwidth=0.17)

    nextButton = Button(win, text="Add question", font=("Arial", 16))
    nextButton.place(relx=0.55, rely=0.85, relheight=0.1, relwidth=0.22)

    cancelButton = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelButton.place(relx=0.23, rely=0.85, relheight=0.1, relwidth=0.2)

    questionEntry.focus()
    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    createAssign("Kostas Papadopoulos")
    # createQs("Test", "Kostas Papadopoulos")
    pass
