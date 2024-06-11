"""
This is a test
It will list all students on a window that a certain teacher has signed up
You will be able to select students
"""

from tkinter import *
import psycopg2
import os
from dotenv import load_dotenv


def createWin(teacher):
    win = Tk()
    win.geometry("500x500")
    win.title("TEST_ListStudents")

    titleLabel = Label(win, text="Students:", font="Arial 16 bold")
    titleLabel.pack()

    scroll = Scrollbar(win)
    scroll.pack(side=RIGHT, fill=Y)

    students = sql(teacher)
    stuList = Listbox(win, selectmode=MULTIPLE, width=30, height=20, borderwidth=0, bg='#f0f0f0', font="Arial 16",
                      yscrollcommand=scroll.set)
    for student in students:
        stuList.insert(END, student)
    stuList.pack(side=LEFT, fill=BOTH)

    def select():
        selected = stuList.curselection()
        for i in selected:
            print(stuList.get(i))

    # CHANGE TO GET AND RETURN THE VALUES
    printButton = Button(win, text="Print Selected", command=select)
    printButton.pack()

    scroll.config(command=stuList.yview)
    win.resizable(False, False)
    win.mainloop()

def sql(teacher):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM main_acc WHERE teacher = '{teacher}'")
        res = cur.fetchall()
        if res is not None:
            return [row[0] for row in res]  # Return the list of student names
        else:
            return []
    except Exception as e:
        print("Connection Failed", "Unable to fetch students.")
        return []


if __name__ == "__main__":
    createWin("admin_kostas")
