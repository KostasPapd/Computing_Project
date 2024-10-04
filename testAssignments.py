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

def database(tID, cID, sID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()

        # checks if student is in the class
        cur.execute(f"SELECT * FROM main_acc WHERE id = '{sID}' AND class_id = '{cID}'")
        inClass = cur.fetchone()
        if not inClass:
            mg.showwarning("Not Enrolled", "Student is not enrolled in this class.")
            return []


        # check if the teacher has any assignments for the class
        cur.execute(f"SELECT * FROM assignments WHERE teacher_id = '{tID}' AND class_id = '{cID}'")
        data = cur.fetchall()
        return data
    except Exception as e:
        mg.showwarning("Connection Failed", e)
        return []

def createTable(tID, cID, sID):
    win = Tk()

    win.title("Test Assignments List")

    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    assignLabel = Label(win, text="Assignments", font=("Arial", 20))
    assignLabel.pack()

    assignments = database(tID, cID, sID)

    if not assignments:
        Label(win, text="No assignments found.", font=("Arial", 16)).pack()
    else:
        for i in range(len(assignments)):
            Button(win, text=f"Assignment: {assignments[i][1]} , Due: {assignments[i][3]}", font=("Arial", 16),
                   command=lambda: Questions.nextQ(assignments[i])).pack()

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    createTable("1", "1", "1")
