from tkinter import *
import logInMenu
import processWindows
from tkinter import messagebox as mg
import psycopg2
import os
from dotenv import load_dotenv
from SQLfunctions import getIDs, getID
from questions import Questions

# ADD CLASS TO CREATE MENU BAR
"""
Add the assignments list to the student view
"""

def signOut(win):
    win.destroy()
    logInMenu.createLogIn()

def getAssignments(tID, sID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()

        cur.execute(f"SELECT id FROM stud_classes WHERE teacher_id = '{tID}'")
        class_id = cur.fetchall()

        names = []
        for i in range(len(class_id)):
            cur.execute(f"SELECT class_names FROM stud_classes WHERE id = '{class_id[i][0]}'")
            names.append(cur.fetchall()[0][0])

        valid_ids = []
        for name in range(len(names)):
            cur.execute(f'SELECT 1 FROM "{names[name]}_1" WHERE student_id = %s', (sID,))
            result = cur.fetchone()
            if result:
                cur.execute(f"SELECT id FROM stud_classes WHERE class_names = '{names[name]}'")
                valid_ids.append(cur.fetchone()[0])

        assignments = []
        for id in range(len(valid_ids)):
            cur.execute(f"SELECT * FROM assignments WHERE teacher_id = '{tID}' AND class_id = '{valid_ids[id]}'")
            data = cur.fetchall()
            for assignment in data:
                cur.execute(f"SELECT 1 FROM submissions WHERE assignment_id = %s AND student_id = %s", (assignment[0], sID))
                if not cur.fetchone():
                    assignments.append(assignment)

        return assignments
    except Exception as e:
        mg.showwarning("Connection Failed", e)
        return []

def openAssign(win, tID, assignments, sID, password):
    instance = Questions(tID, 1, assignments[5], sID, password)
    win.destroy()
    instance.createWindow()

class Assignments(Frame):
    def __init__(self, master=None, tID=None, sID=None, password=None):
        super().__init__(master)
        self.tID = tID
        self.sID = sID
        self.password = password
        self.pack()
        self.showAssign()

    def showAssign(self):
        self.label = Label(self, text="Your Assignments", font=("Helvetica", 20))
        self.label.pack()  # Pack puts it at the top of the page

        assignments = getAssignments(self.tID, self.sID)

        if not assignments:
            Label(self, text="No assignments found.", font=("Arial", 16)).pack()
        else:
            for i in range(len(assignments)):
                Button(self, text=f"Assignment: {assignments[i][1]} , Due: {assignments[i][3]}", font=("Arial", 16),
                       command=lambda a=assignments[i]: openAssign(self.master, self.tID, a, self.sID, self.password)).pack()



class MenuBar(Frame):
    def __init__(self, email="", password="", id=""):
        super().__init__()
        self.email = email
        self.passw = password
        self.id = id
        self.pack()
        self.toolBarMenu()
        self.frames = {}

    def toolBarMenu(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)

        accMenu.add_command(label="Change Email", font=("Helvetica", 10),
                            command=lambda: processWindows.changeEmailUI(self.email, "Student"))
        accMenu.add_command(label="Change Password", font=("Helvetica", 10),
                            command=lambda: processWindows.changePassUI(self.email, self.passw, "Student"))
        accMenu.add_command(label="- " * 15, font=("Helvetica", 10))
        accMenu.add_command(label="Sign Out", font=("Helvetica", 10), command=lambda: signOut(self.master))

        toolBar.add_cascade(label="Progress", command=lambda: processWindows.studentProgress(self.id))
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

#def createStudent(name, id, password):
 #   win = Tk()
  #  nameText = name
   # win.title(f"The Physics Lab - {name}")
    #wWidth = 300
    #wHeight = 300
    #xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    #yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    #win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    #label = Label(win, text="Student view", font=("Helvetica", 20))
    #label.place(relx=0.5, rely=0.5, anchor="center")


def createStudent(name, email, password):
    win = Tk()
    win.title(f"The Physics Lab - {name}")
    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    s_id = getID(email)
    toolB = MenuBar(email, password, s_id)

    studentID = getIDs(name)[0]
    teacherID = getIDs(name)[1]

    Assignments(win, teacherID, studentID, password)

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createStudent("Kostas Papadopoulos", "kostispapd@outlook.com", "password")
    pass
