from tkinter import *
import logInMenu
import processWindows
from tkinter import messagebox as mg
import psycopg2
import os
from dotenv import load_dotenv
from SQLfunctions import getIDs
from questions import Questions

# ADD CLASS TO CREATE MENU BAR
"""
Add the assignments list to the student view
"""

def signOut(win):
    win.destroy()
    logInMenu.createLogIn()

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

class Assignments(Frame):
    def __init__(self, master=None, tID=None, sID=None):
        super().__init__(master)
        self.tID = tID
        self.sID = sID
        self.pack()
        self.showAssign()

    def showAssign(self):
        self.label = Label(self, text="Your Assignments", font=("Helvetica", 20))
        self.label.pack()  # Pack puts it at the top of the page

        assignments = database(self.tID, self.sID)

        if not assignments:
            Label(self, text="No assignments found.", font=("Arial", 16)).pack()
        else:
            for i in range(len(assignments)):
                Button(self, text=f"Assignment: {assignments[i][1]} , Due: {assignments[i][3]}", font=("Arial", 16),
                       command=lambda: openAssign(self.master, self.tID, assignments)).pack()



class MenuBar(Frame):
    def __init__(self, email="", password=""):
        super().__init__()
        self.email = email
        self.passw = password
        self.pack()
        self.toolBarMenu()
        self.frames = {}

    def toolBarMenu(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)

        # accMenu.add_command(label="Join Class", font=("Helvetica", 10)) - maybe do
        accMenu.add_command(label="Change Email", font=("Helvetica", 10),
                            command=lambda: processWindows.changeEmailUI(self.email, "Student"))
        # ADD COMMAND THAT CHANGES EMAIL TO SQL PROGRAM
        accMenu.add_command(label="Change Password", font=("Helvetica", 10),
                            command=lambda: processWindows.changePassUI(self.email, self.passw, "Student"))
        # ADD COMMAND THAT CHANGES PASSWORD TO SQL PROGRAM
        accMenu.add_command(label="- " * 15, font=("Helvetica", 10))
        accMenu.add_command(label="Sign Out", font=("Helvetica", 10), command=lambda: signOut(self.master))

        toolBar.add_cascade(label="Settings", menu=accMenu)
        toolBar.add_command(label="Exit", command=self.exit)

    def hide(self):
        for frame in self.frames.values():
            frame.pack_forget()

    def showAssign(self):
        self.hide()
        if "assignments" not in self.frames:
            self.frames["assignments"] = Assignments(self.master)
        self.frames["assignments"].pack(fill="both", expand=True)

    def exit(self):
        self.quit()



def createStudent(name, email, password):
    win = Tk()
    nameText = name
    win.title(f"The Physics Lab - {name}")
    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    toolB = MenuBar(email, password)

    studentID = getIDs(name)[0]
    teacherID = getIDs(name)[1]

    Assignments(win, teacherID, studentID)

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createStudent("Kostas Papadopoulos", "email", "password")
    pass
