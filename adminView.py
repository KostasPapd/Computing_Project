from tkinter import *
import logInMenu
from processWindows import changeEmailUI, changePassUI, createClassUI, deleteClassUI, submissionViewCreate, createAssign, createBox

"""
Using a class to create a menu bar is a very good idea. It is easier to upkeep and read the code and makes it easier to 
add more commands to the menu bar.
"""


class MenuBar(Frame):
    # constructor
    def __init__(self, user="", password="", id=None):
        # calls the constructor of the parent frame class
        super().__init__()
        # stores the parameters as instance variables
        self.user = user
        self.passw = password
        self.id = id
        # calls the method to create the menu bar
        self.toolBarMenu()

    def toolBarMenu(self):
        # creates a menu bar instance and sets it to the top of the window
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        # account menu creation and addition of commands
        accMenu = Menu(toolBar)
        accMenu.add_command(label="Create Student Account",  font=("Helvetica", 9),
                            command=lambda: createBox(self.id))
        accMenu.add_command(label="- "*18, font=("Helvetica", 9))
        accMenu.add_command(label="Your Account:", font=("Helvetica", 9))
        accMenu.add_command(label="Change Email", font=("Helvetica", 9),
                            command=lambda: changeEmailUI(self.user, "Admin"))
        accMenu.add_command(label="Change Password", font=("Helvetica", 9),
                            command=lambda: changePassUI(self.user, "Admin"))

        # class menu creation and addition of commands
        classMenu = Menu(toolBar)
        classMenu.add_command(label="Create Class", font=("Helvetica", 9),
                              command=lambda: createClassUI(self.id))
        classMenu.add_command(label="Delete Class", font=("Helvetica", 9),
                              command=lambda: deleteClassUI(self.id))

        # addition of the menus to the menu bar
        toolBar.add_cascade(label="Accounts", menu=accMenu)
        toolBar.add_cascade(label="Classes", menu=classMenu)
        toolBar.add_command(label="Sign Out", command=self.signOut)
        toolBar.add_command(label="Exit", command=self.exit)

    # method to exit the program
    def exit(self):
        self.quit()

    #method to sign out
    def signOut(self, ):
        self.master.destroy()
        logInMenu.createLogIn()

#def createView(name, id, password):
#    win = Tk()
 #   nameText = name
  #  win.title(f"The Physics Lab - Admin")
   # wWidth = 300
    #wHeight = 300
    #xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    #yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    #win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    #label = Label(win, text="Admin view", font=("Helvetica", 20))
    #label.place(relx=0.5, rely=0.5, anchor="center")

def createView(teach_id, password, user):
    win = Tk() # creates window instance
    win.title("The Physics Lab - Admin")
    # works out the center of the screen and places window there
    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    # creates a menu bar instance
    toolB = MenuBar(user, password, teach_id)

    # creates a label with the welcome message
    welcomeLabel = Label(win, text=f"Welcome, {user}", font=("Helvetica", 20))
    welcomeLabel.place(relx= 0.0, rely= 0.02, relheight= 0.1, relwidth= 1)

    # creates a button to create an assignment
    createAssignButtton = Button(win, text="Create Assignment", font=("Helvetica", 18),
                                 command=lambda: createAssign(teach_id))
    createAssignButtton.place(relx=0.25, rely=0.2, relheight=0.1, relwidth=0.5)

    # creates a button to view assignments and submissions
    viewAssignButton = Button(win, text="View Assignments", font=("Helvetica", 18), command=lambda: submissionViewCreate(teach_id))
    viewAssignButton.place(relx=0.25, rely=0.4, relheight=0.1, relwidth=0.5)

    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createView(1, "password", "testing account")
    pass
