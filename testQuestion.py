from tkinter import *
from tkinter import messagebox as mg
from tkinter import filedialog, ttk
import psycopg2
import os
from dotenv import load_dotenv

from SQLfunctions import checkType


def pullQuestions(assignment, questionNum):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT question, marks, question_type FROM {assignment} WHERE question_id = {questionNum}")
        data = cur.fetchall()
        return data[0]
    except Exception as e:
        mg.showwarning("Connection Failed", e)


def createWindow(assignName, questionNum):
    win = Tk()

    win.title("Test Questions")

    wWidth = 750
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    answerLabel = Label(win, text="Answer:", font=("Arial", 20))
    answerLabel.place(relx=0.05, rely=0.15)

    def open_file_dialog():
        filename = filedialog.askopenfilename()


    if checkType(assignName, questionNum) == "Standard answer":
        orLabel = Label(win, text="or (show all working out)", font=("Arial", 20))
        orLabel.place(relx=0.5, rely=0.15)
        answerButton = Button(win, text="Upload Answer", font=("Arial", 18), command=lambda: open_file_dialog())
        answerButton.place(relx=0.2, rely=0.14, relheight=0.1, relwidth=0.25)
        answerEntry = Text(win, font=("Arial", 14))
        answerEntry.place(relx=0.2, rely=0.3, relheight=0.4, relwidth=0.7)


    data = pullQuestions(assignName, questionNum)
    questionLabel = Label(win, text=data[0], font=("Arial", 20))
    questionLabel.pack()

    win.resizable(False, False)
    win.mainloop()


def main(assignName, questionNum):
    questionNum += 1
    createWindow(assignName, questionNum)

if __name__ == "__main__":
    main("test_assignment", 0)
