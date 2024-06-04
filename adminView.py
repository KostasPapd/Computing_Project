from tkinter import *
import registerMenu
import createMainMenu

def testSendEmail(email):
    # https://automatetheboringstuff.com/2e/chapter18/
    # https://mailtrap.io/blog/python-send-email/
    pass

def searchAcc():
    win = Toplevel()
    win.title("Search Account")
    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleLabel = Label(win, text="Search for student account details", font=("Arial", 18))
    titleLabel.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

    emailLabel = Label(win, text="Student Email:", font=("Arial", 15))
    emailLabel.place(relx=0.03, rely=0.35, relheight=0.1, relwidth=0.3)

    emailBox = Entry(win, font=("Helvetica", 12))
    emailBox.place(relx=0.32, rely=0.36, relheight=0.08, relwidth=0.62)

    searchButton = Button(win, text="Search for account", font=("Arial", 15), command=lambda: showDet(emailBox.get(),
                                                                                                      win))
    searchButton.place(relx=0.15, rely=0.6, relheight=0.16, relwidth=0.4)

    backButton = Button(win, text="Back", font=("Arial", 15), command=lambda: win.destroy())
    backButton.place(relx=0.65, rely=0.6, relheight=0.16, relwidth=0.2)

    emailBox.focus()
    win.resizable(False, False)
    win.mainloop()

def showDet(email, window):
    from SQLfunctions import returnDetails, checkEmail
    from tkinter import messagebox as mg
    window.destroy()
    win = Toplevel()
    win.title("Account Details")
    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleLabel = Label(win, text="Student Account Details", font=("Arial", 18))
    titleLabel.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

    #if checkEmail(email) == True:
    #    mg.showwarning("Account not found", "The account does not exist")
    #else:
    details = returnDetails(email)

    nameLabel = Label(win, text=f"Name: {details[0]}", font=("Arial", 15))
    passLabel = Label(win, text=f"Password: {details[1]}", font=("Arial", 15))
    emailLabel = Label(win, text=f"Email: {details[2]}", font=("Arial", 15))

    nameLabel.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.8)
    emailLabel.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)
    passLabel.place(relx=0.1, rely=0.5, relheight=0.1, relwidth=0.8)

    emailBut = Button(win, text="Email to student", font=("Arial", 15))  # ADD COMMAND
    emailBut.place(relx=0.1, rely=0.75, relheight=0.16, relwidth=0.4)

    exitBut = Button(win, text="Exit", font=("Arial", 15), command=lambda: win.destroy())
    exitBut.place(relx=0.65, rely=0.75, relheight=0.16, relwidth=0.2)


    win.resizable(False, False)
    win.mainloop()


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
        accMenu.add_command(label="Search for account", font=("Helvetica", 10), command=lambda: searchAcc())
        accMenu.add_command(label="- "*18, font=("Helvetica", 10))
        accMenu.add_command(label="Your Account:", font=("Helvetica", 10))
        accMenu.add_command(label="Change Email", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES EMAIL TO SQL PROGRAM
        accMenu.add_command(label="Change Password", font=("Helvetica", 10))
        # ADD COMMAND THAT CHANGES PASSWORD TO SQL PROGRAM

        toolBar.add_cascade(label="Accounts", menu=accMenu)
        toolBar.add_command(label="Sign Out", command=lambda: signOut(self.master))
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
