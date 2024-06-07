from tkinter import *
import registerMenu
import logInMenu
from processWindows import *

def signOut(win):
    win.destroy()
    logInMenu.createLogIn()


"""
Using a class to create a menu bar is a very good idea. It is easier to upkeep and read the code and makes it easier to 
add more commands to the menu bar.
"""


class MenuBar(Frame):
    def __init__(self, user="", password=""):
        super().__init__()
        self.user = user
        self.passw = password
        self.toolBarMenu()

    def toolBarMenu(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)
        accMenu.add_command(label="Create Student Account",  font=("Helvetica", 10),
                            command=lambda: registerMenu.createBox())
        accMenu.add_command(label="- "*18, font=("Helvetica", 10))
        accMenu.add_command(label="Your Account:", font=("Helvetica", 10))
        accMenu.add_command(label="Change Email", font=("Helvetica", 10),
                            command=lambda: changeEmailUI(self.user, "Admin"))
        # ADD COMMAND THAT CHANGES EMAIL TO SQL PROGRAM
        accMenu.add_command(label="Change Password", font=("Helvetica", 10),
                            command=lambda: changePassUI(self.user, self.passw, "Admin"))
        # ADD COMMAND THAT CHANGES PASSWORD TO SQL PROGRAM

        toolBar.add_cascade(label="Accounts", menu=accMenu)
        toolBar.add_command(label="Sign Out", command=lambda: signOut(self.master))
        toolBar.add_command(label="Exit", command=self.exit)

    def exit(self):
        self.quit()


def createView(user, password):
    win = Tk()
    win.title("The Physics Lab - Admin")
    win.geometry("500x500")
    toolB = MenuBar(user, password)

    win.state("zoomed")
    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createView("test", "password")
    pass
