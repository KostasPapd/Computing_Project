from tkinter import *
import registerMenu
import logInMenu
from processWindows import changeEmailUI, changePassUI, createClassUI

def signOut(win):
    win.destroy()
    logInMenu.createLogIn()


"""
Using a class to create a menu bar is a very good idea. It is easier to upkeep and read the code and makes it easier to 
add more commands to the menu bar.
"""


class MenuBar(Frame):
    def __init__(self, user="", password="", name=""):
        super().__init__()
        self.user = user
        self.passw = password
        self.name = name
        self.toolBarMenu()

    def toolBarMenu(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)
        accMenu.add_command(label="Create Student Account",  font=("Helvetica", 9),
                            command=lambda: registerMenu.createBox(self.name))
        accMenu.add_command(label="- "*18, font=("Helvetica", 9))
        accMenu.add_command(label="Your Account:", font=("Helvetica", 9))
        accMenu.add_command(label="Change Email", font=("Helvetica", 9),
                            command=lambda: changeEmailUI(self.user, "Admin"))
        accMenu.add_command(label="Change Password", font=("Helvetica", 9),
                            command=lambda: changePassUI(self.user, self.passw, "Admin"))

        classMenu = Menu(toolBar)
        classMenu.add_command(label="Create Class", font=("Helvetica", 9),
                              command=lambda: createClassUI(self.name))
        classMenu.add_command(label="Delete Class", font=("Helvetica", 9))

        toolBar.add_cascade(label="Accounts", menu=accMenu)
        toolBar.add_cascade(label="Classes", menu=classMenu)
        toolBar.add_command(label="Assignments")
        toolBar.add_command(label="Sign Out", command=lambda: signOut(self.master))
        toolBar.add_command(label="Exit", command=self.exit)

    def exit(self):
        self.quit()


def createView(user, password, name):
    win = Tk()
    win.title("The Physics Lab - Admin")
    win.geometry("500x500")
    toolB = MenuBar(user, password, name)

    win.state("zoomed")
    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createView("test", "password", "test name")
    pass
