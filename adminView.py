from tkinter import *
import registerMenu
import createMainMenu

def testSendEmail(email):
    # https://automatetheboringstuff.com/2e/chapter18/
    # https://mailtrap.io/blog/python-send-email/
    pass


def signOut(win):
    win.destroy()
    createMainMenu.createMenu()


"""
Using a class to create a menu bar is a very good idea. It is easier to upkeep and read the code and makes it easier to 
add more commands to the menu bar.
"""

class MenuBar(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)
        accMenu.add_command(label="Create Student Account",  font=("Helvetica", 10),
                            command=lambda: registerMenu.createBox())
        accMenu.add_command(label="- "*18, font=("Helvetica", 10))
        accMenu.add_command(label="Your Account:", font=("Helvetica", 10))
        accMenu.add_command(label="Change Password", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES PASSWORD TO SQL PROGRAM
        accMenu.add_command(label="Change Email", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES EMAIL TO SQL PROGRAM
        accMenu.add_command(label="Change Name", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES NAME TO SQL PROGRAM
        accMenu.add_command(label="Sign Out", font=("Helvetica", 10), command=lambda: signOut(self.master))

        toolBar.add_cascade(label="Accounts", menu=accMenu)
        toolBar.add_command(label="Exit", command=self.exit)



    def exit(self):
        self.quit()


def createView():
    win = Tk()
    win.title("Admin view")
    win.geometry("500x500")
    toolB = MenuBar()

    exitButton = Button(win, text="Exit", command=lambda: win.destroy())
    exitButton.config(font=("Arial", 20))
    exitButton.place(relx=0.37, rely=0.6, relheight=0.11, relwidth=0.23)



    win.attributes("-fullscreen", True)
    win.resizable(False, False)
    win.mainloop()

createView()
