from tkinter import *
import registerMenu
import logInMenu

def sendEmailCreate(email, password, name):
    import smtplib

    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("physics12305@outlook.com", "PhysicsEmail1")

    sender = "physics12305@outlook.com"
    receiver = email
    message = (f"Subject: Account Created\n\nYour teacher has created an account for you. Your details are below:\n\n"
               f"Name: {name}\nPassword: {password}\nEmail: {email}\n\n"
               f"Make sure to log in and change your password to something more secure. "
               f"Please keep this information safe and do not share it with anyone.")

    smtpObj.sendmail(sender, receiver, message)
    smtpObj.quit()


def sendEmailSearch(email, name, password):
    # Add code that send email with account details
    pass

def searchAcc():
    win = Toplevel()
    win.title("Search Account")
    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleLabel = Label(win, text="Send student account details", font=("Arial", 18))
    titleLabel.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

    emailLabel = Label(win, text="Student Email:", font=("Arial", 15))
    emailLabel.place(relx=0.03, rely=0.35, relheight=0.1, relwidth=0.3)

    emailBox = Entry(win, font=("Helvetica", 12))
    emailBox.place(relx=0.32, rely=0.36, relheight=0.08, relwidth=0.62)

    searchButton = Button(win, text="Send details to student", font=("Arial", 15),
                          command=lambda: sendEmail(emailBox.get()))
    searchButton.place(relx=0.12, rely=0.6, relheight=0.16, relwidth=0.45)

    backButton = Button(win, text="Back", font=("Arial", 15), command=lambda: win.destroy())
    backButton.place(relx=0.65, rely=0.6, relheight=0.16, relwidth=0.2)

    emailBox.focus()
    win.resizable(False, False)
    win.mainloop()

def sendEmail(email):
    from SQLfunctions import returnDetails, checkEmail
    from tkinter import messagebox as mg

    if checkEmail(email) == False:
        details = returnDetails(email)
        sendEmailSearch(email, details[0], details[1])
        mg.showinfo("Email Sent", "The email has been sent to the student.")
    else:
        mg.showwarning("Email not found", "The email you entered does not exist in the database.")


def signOut(win):
    win.destroy()
    logInMenu.createLogIn()


"""
Using a class to create a menu bar is a very good idea. It is easier to upkeep and read the code and makes it easier to 
add more commands to the menu bar.
"""

class MenuBar(Frame):
    def __init__(self):
        super().__init__()
        self.toolBarMenu()

    def toolBarMenu(self):
        toolBar = Menu(self.master)
        self.master.config(menu=toolBar)

        accMenu = Menu(toolBar)
        accMenu.add_command(label="Create Student Account",  font=("Helvetica", 10),
                            command=lambda: registerMenu.createBox())
        accMenu.add_command(label="Send account details", font=("Helvetica", 10), command=lambda: searchAcc())
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
    win.title("The Physics Lab - Admin")
    win.geometry("500x500")
    toolB = MenuBar()

    win.state("zoomed")
    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    # Testing
    createView()
    # sendEmailCreate("kostispapd@outlook.com", "password", "Test Name")
    pass
