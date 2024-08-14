"""
This file is used to create a window that displays a list of assignments under a certain
teacher's name. This is a test file.
"""

from tkinter import *
from tkinter import messagebox as mg
import psycopg2
import os
from dotenv import load_dotenv

def database(tID, cID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM assignments WHERE teacher_id = '{tID}' AND class_id = '{cID}'")
        data = cur.fetchall()
        return data
    except Exception as e:
        mg.showwarning("Connection Failed", e)

def createTable(tID, cID):
    win = Tk()

    win.title("Test Assignments List")

    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    assignLabel = Label(win, text="Assignments", font=("Arial", 20))
    assignLabel.pack()

    assignments = database(tID, cID)

    for i in range(len(assignments)):
        Button(win, text=f"Assignment: {assignments[i][1]} , Due: {assignments[i][3]}", font=("Arial", 16)).pack()

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    createTable("1", "1")
