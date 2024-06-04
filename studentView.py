from tkinter import *
from tkinter.tix import *
from createMainMenu import createMenu

# ADD CLASS TO CREATE MENU BAR

def signOut(win):
    win.destroy()
    createMenu()

class MenuBar(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

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

        toolBar.add_cascade(label="Assignments")  # ADD COMMAND THAT SHOWS ASSIGNMENTS
        toolBar.add_cascade(label="Statistics")  # ADD COMMAND THAT SHOWS STATISTICS
        toolBar.add_cascade(label="Settings", menu=accMenu)
        toolBar.add_command(label="Exit", command=self.exit)

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
createStudent("")