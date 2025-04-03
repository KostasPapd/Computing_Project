# for UI
from tkinter import *
from tkinter import messagebox as mg
# for signing out
import logInMenu
# for different windows and processes
import processWindows
# for database connection
import psycopg2
import os
from dotenv import load_dotenv
# for different database functions
from SQLfunctions import getIDs, getID
# for answering assignments
from questions import Questions

# ADD CLASS TO CREATE MENU BAR
"""
Add the assignments list to the student view
"""
def getAssignments(tID, sID):
    load_dotenv() # loads env file and gets the database key
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key) # connect to the database
        cur = conn.cursor() # creates a cursor
        cur.execute(f"SELECT id FROM stud_classes WHERE teacher_id = '{tID}'") # gets class ids
        class_id = cur.fetchall()
        names = []
        for i in range(len(class_id)):
            cur.execute(f"SELECT class_names FROM stud_classes WHERE id = '{class_id[i][0]}'") # gets class names
            names.append(cur.fetchall()[0][0])
        valid_ids = []
        for name in range(len(names)):
            cur.execute(f'SELECT 1 FROM "{names[name]}" WHERE student_id = %s', (sID,)) # checks if the student is in the class
            result = cur.fetchone()
            if result:
                cur.execute(f"SELECT id FROM stud_classes WHERE class_names = '{names[name]}'") # gets the class id (the ones that the student is in)
                valid_ids.append(cur.fetchone()[0])
        assignments = []
        for id in range(len(valid_ids)):
            cur.execute(f"SELECT * FROM assignments WHERE teacher_id = '{tID}' AND class_id = '{valid_ids[id]}'") # gets the assignment info
            data = cur.fetchall()
            for assignment in data:
                cur.execute(f"SELECT 1 FROM submissions WHERE assignment_id = %s AND student_id = %s", (assignment[0], sID)) # check if the student has completed the assignment
                if not cur.fetchone():
                    assignments.append(assignment)
        return assignments # returns the assignments
    except Exception as e:
        # error handling
        mg.showwarning("Connection Failed", e)
        return []

def openAssign(win, tID, assignments, sID, password):
    instance = Questions(tID, 1, assignments[5], sID, password) # defines window instance
    win.destroy() # destroys the current window
    instance.createWindow() # creates the insance of the Questions class

class Assignments(Frame):
    def __init__(self, master=None, tID=None, sID=None, password=None):
        # constructor
        super().__init__(master)
        self.tID = tID
        self.sID = sID
        self.password = password
        self.pack()
        self.showAssign()
    # function to show the assignments
    def showAssign(self):
        self.label = Label(self, text="Your Assignments", font=("Helvetica", 20))
        self.label.pack()  # Pack puts it at the top of the page

        assignments = getAssignments(self.tID, self.sID) # gets assignments from the database

        if not assignments:
            Label(self, text="No assignments found.", font=("Arial", 16)).pack()
        else:
            for i in range(len(assignments)):
                Button(self, text=f"Assignment: {assignments[i][1]} , Due: {assignments[i][3]}", font=("Arial", 16),
                       command=lambda a=assignments[i]: openAssign(self.master, self.tID, a, self.sID, self.password)).pack()



class MenuBar(Frame):
    def __init__(self, email="", password="", id=""):
        # constructor
        super().__init__()
        self.email = email
        self.passw = password
        self.id = id
        self.pack()
        self.toolBarMenu()
        self.frames = {}

    def toolBarMenu(self):
        # creates a menu bar instance and sets it to the top of the window
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)
        # account menu creation and addition of commands
        accMenu = Menu(toolBar)

        accMenu.add_command(label="Change Email", font=("Helvetica", 10),
                            command=lambda: processWindows.changeEmailUI(self.email, "Student"))
        accMenu.add_command(label="Change Password", font=("Helvetica", 10),
                            command=lambda: processWindows.changePassUI(self.email, "Student"))
        accMenu.add_command(label="- " * 15, font=("Helvetica", 10))
        accMenu.add_command(label="Sign Out", font=("Helvetica", 10), command=lambda: self.signOut())
        # adds commands to toolbar
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

    def signOut(self):
        self.master.destroy()
        logInMenu.createLogIn()

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
    win = Tk() # window instance
    win.title(f"The Physics Lab - {name}") # title
    # finds center of screen and sets window to that position
    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # gets teacher and student id from name
    studentID = getIDs(name)[0]
    teacherID = getIDs(name)[1]

    toolB = MenuBar(email, password, studentID) # toolbar instance

    # creates an assignments frame instance
    Assignments(win, teacherID, studentID, password)

    win.resizable(False, False)
    win.mainloop()

if __name__ == "__main__":
    # Testing
    createStudent("Kostas Papadopoulos", "kostispapd@outlook.com", "password")
    pass
