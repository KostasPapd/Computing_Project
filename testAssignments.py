"""
This file is used to create a window that displays a list of assignments under a certain
teacher's name. This is a test file.

FIX THIS
"""

from tkinter import *
from tkinter import messagebox as mg
import psycopg2
import os
from dotenv import load_dotenv
from testQuestOOP import Questions

def database(tID, sID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()

        cur.execute(f"SELECT class_id FROM main_acc WHERE id = '{sID}'")
        classID = cur.fetchone()[0]

        # check if the teacher has any assignments for the class
        cur.execute(f"SELECT * FROM assignments WHERE teacher_id = '{tID}' AND class_id = '{classID}'")
        data = cur.fetchall()
        return data
    except Exception as e:
        mg.showwarning("Connection Failed", e)
        print(e)
        return []

def openAssign(win, tID, assignments):
    instance = Questions(tID, 1, assignments[0][5])
    win.destroy()
    instance.createWindow()

def createTable(tID, sID):
    win = Tk()

    win.title("Test Assignments List")

    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    assignLabel = Label(win, text="Assignments", font=("Arial", 20))
    assignLabel.pack()

    assignments = database(tID, sID)

    if not assignments:
        Label(win, text="No assignments found.", font=("Arial", 16)).pack()
    else:
        for i in range(len(assignments)):
            Button(win, text=f"Assignment: {assignments[i][1]} , Due: {assignments[i][3]}", font=("Arial", 16),
                   command=lambda: openAssign(win, tID, assignments)).pack()

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    createTable("1",  "3")
