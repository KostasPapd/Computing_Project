from tkinter import *
import registerMenu
import logInMenu
from processWindows import changeEmailUI, changePassUI, createClassUI
from assignProcess import createAssign

def signOut(win):
    win.destroy()
    logInMenu.createLogIn()


"""
Using a class to create a menu bar is a very good idea. It is easier to upkeep and read the code and makes it easier to 
add more commands to the menu bar.
"""


class MenuBar(Frame):
    def __init__(self, user="", password="", id=None):
        super().__init__()
        self.user = user
        self.passw = password
        self.id = id
        self.toolBarMenu()

    def toolBarMenu(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)
        accMenu.add_command(label="Create Student Account",  font=("Helvetica", 9),
                            command=lambda: registerMenu.createBox(self.id))
        accMenu.add_command(label="- "*18, font=("Helvetica", 9))
        accMenu.add_command(label="Your Account:", font=("Helvetica", 9))
        accMenu.add_command(label="Change Email", font=("Helvetica", 9),
                            command=lambda: changeEmailUI(self.user, "Admin"))
        accMenu.add_command(label="Change Password", font=("Helvetica", 9),
                            command=lambda: changePassUI(self.user, self.passw, "Admin"))

        classMenu = Menu(toolBar)
        classMenu.add_command(label="Create Class", font=("Helvetica", 9),
                              command=lambda: createClassUI(self.id))
        classMenu.add_command(label="Delete Class", font=("Helvetica", 9))

        toolBar.add_cascade(label="Accounts", menu=accMenu)
        toolBar.add_cascade(label="Classes", menu=classMenu)
        toolBar.add_command(label="Sign Out", command=lambda: signOut(self.master))
        toolBar.add_command(label="Exit", command=self.exit)

    def exit(self):
        self.quit()


def createView(teach_id, password, user):
    win = Tk()
    win.title("The Physics Lab - Admin")
    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    toolB = MenuBar(user, password, teach_id)

    welcomeLabel = Label(win, text=f"Welcome, {user}", font=("Helvetica", 20))
    welcomeLabel.place(relx= 0.0, rely= 0.02, relheight= 0.1, relwidth= 1)

    createAssignButtton = Button(win, text="Create Assignment", font=("Helvetica", 18),
                                 command=lambda: createAssign(teach_id))
    createAssignButtton.place(relx=0.25, rely=0.2, relheight=0.1, relwidth=0.5)

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createView("test", "password", 1)
    pass
