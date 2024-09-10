from tkinter import *
import logInMenu
import processWindows

# ADD CLASS TO CREATE MENU BAR
"""
Add the assignments list to the student view
"""

def signOut(win):
    win.destroy()
    logInMenu.createLogIn()

class Assignments(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.widgets()

    def widgets(self):
        self.label = Label(self, text="Your Assignments", font=("Helvetica", 20))
        self.label.pack()  # Pack puts it at the top of the page


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

        # toolBar.add_cascade(label="Assignments", command=self.showAssign)  # ADD COMMAND THAT SHOWS ASSIGNMENTS
        # toolBar.add_cascade(label="Statistics", command=self.showStats)  # ADD COMMAND THAT SHOWS STATISTICS
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

    Assignments()

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createStudent("Kostas Papadopoulos", "email", "password")
    pass
