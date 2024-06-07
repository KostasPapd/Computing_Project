"""
The UI for many of the processes will go in here

Add:
Change Password - get value and validation
Change Email - get value and validation
"""

import tkinter
from tkinter import *
import smtplib
from tkinter import messagebox as mg


def changePassUI(user, password, level):
    win = Toplevel()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Change Password")

    chaLabel = Label(win, text="Change Password", font=("Arial", 20))
    chaLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    newPassLabel = Label(win, text="New Password:", font=("Arial", 16))
    newPassLabel.place(relx=0.09, rely=0.3, relheight=0.13, relwidth=0.3)
    newPassVar = tkinter.StringVar()
    newPassBox = Entry(win, textvariable=newPassVar, font=('Arial', 12), show='•', width=27)
    newPassBox.place(relx=0.4, rely=0.34, relheight=0.06, relwidth=0.48)

    rePassLabel = Label(win, text="Re-Type Password:", font=("Arial", 14))
    rePassLabel.place(relx=0.02, rely=0.5, relheight=0.13, relwidth=0.4)
    rePassVar = tkinter.StringVar()
    rePassBox = Entry(win, textvariable=rePassVar, font=('Arial', 12), show='•', width=27)
    rePassBox.place(relx=0.4, rely=0.54, relheight=0.06, relwidth=0.48)

    changeBut = Button(win, text="Change Password", font=("Arial", 16))
    # Add command that runs a value checker and then runs the SQL to change the database
    changeBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    newPassBox.focus()
    win.resizable(False, False)
    win.mainloop()


def changeEmailUI(user, level):
    win = Toplevel()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Change Email")

    chaLabel = Label(win, text="Change Email", font=("Arial", 20))
    chaLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    newEmailLabel = Label(win, text="New Email:", font=("Arial", 16))
    newEmailLabel.place(relx=0.09, rely=0.3, relheight=0.13, relwidth=0.3)
    newEmailVar = tkinter.StringVar()
    newEmailBox = Entry(win, textvariable=newEmailVar, font=('Arial', 12), width=27)
    newEmailBox.place(relx=0.4, rely=0.34, relheight=0.06, relwidth=0.48)

    reEmailLabel = Label(win, text="Re-Type Email:", font=("Arial", 14))
    reEmailLabel.place(relx=0.02, rely=0.5, relheight=0.13, relwidth=0.4)
    reEmailVar = tkinter.StringVar()
    reEmailBox = Entry(win, textvariable=reEmailVar, font=('Arial', 12), width=27)
    reEmailBox.place(relx=0.4, rely=0.54, relheight=0.06, relwidth=0.48)

    changeBut = Button(win, text="Change Email", font=("Arial", 16))
    # Add command that runs a value checker and then runs the SQL to change the database
    changeBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    newEmailBox.focus()
    win.resizable(False, False)
    win.mainloop()

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
                          command=lambda: sendEmail(emailBox.get(), win))
    searchButton.place(relx=0.12, rely=0.6, relheight=0.16, relwidth=0.45)

    backButton = Button(win, text="Back", font=("Arial", 15), command=lambda: win.destroy())
    backButton.place(relx=0.65, rely=0.6, relheight=0.16, relwidth=0.2)

    emailBox.focus()
    win.resizable(False, False)
    win.mainloop()

def sendEmailCreate(email, password, name):
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("physics12305@outlook.com", "PhysicsEmail1")

    sender = "physics12305@outlook.com"
    receiver = email
    message = (f"Subject: Account Created\n\nYour teacher has created an account for you. Your details are below:\n\n"
               f"Name: {name}\nPassword: {password}\nUsername: {email}\n\n"
               f"Make sure to log in and change your password to something more secure. "
               f"Please keep this information safe and do not share it with anyone.")

    smtpObj.sendmail(sender, receiver, message)
    smtpObj.quit()



if __name__ == "__main__":
    changeEmailUI("test", "test")
