from tkinter import *
from tkinter.tix import *
from createMainMenu import createMenu

# ADD CLASS TO CREATE MENU BAR

def signOut(win):
    win.destroy()
    createMenu()

class Assignments(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.widgets()

    def widgets(self):
        self.label = Label(self, text="Assignments", font=("Helvetica", 20))
        self.label.pack()

class Statistics(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.widgets()

    def widgets(self):
        self.label = Label(self, text="Statistics", font=("Helvetica", 20))
        self.label.pack()

class MenuBar(Frame):
    def __init__(self):
        super().__init__()
        self.pack()
        self.initUI()
        self.frames = {}

    def initUI(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)

        # accMenu.add_command(label="Join Class", font=("Helvetica", 10)) - maybe do
        accMenu.add_command(label="Change Email", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES EMAIL TO SQL PROGRAM
        accMenu.add_command(label="Change Password", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES PASSWORD TO SQL PROGRAM
        accMenu.add_command(label="- " * 15, font=("Helvetica", 10))
        accMenu.add_command(label="Sign Out", font=("Helvetica", 10), command=lambda: signOut(self.master))

        toolBar.add_cascade(label="Assignments", command=self.showAssign)  # ADD COMMAND THAT SHOWS ASSIGNMENTS
        toolBar.add_cascade(label="Statistics", command=self.showStats)  # ADD COMMAND THAT SHOWS STATISTICS
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

    def showStats(self):
        self.hide()
        if "statistics" not in self.frames:
            self.frames["statistics"] = Statistics(self.master)
        self.frames["statistics"].pack(fill="both", expand=True)

    def exit(self):
        self.quit()



def createStudent(name):
    win = Tk()
    win.title("Student View")
    win.geometry("500x500")
    toolB = MenuBar()

    nameText = name
    testLabel = Label(win, text=nameText, font="Arial 60 bold")
    testLabel.place(relx=0.15, rely=0.05, relheight=0.1, relwidth=0.7)


    win.attributes("-fullscreen", True)
    win.resizable(False, False)
    win.mainloop()