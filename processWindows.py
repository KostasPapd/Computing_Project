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
import SQLfunctions


def checkPassword(passw, repassw, level, user, window):
    from isValid import validatePassword
    if passw == repassw:
        if validatePassword(passw) == True:
            SQLfunctions.changePass(user, level, passw)
            mg.showinfo("Password Changed", "Password has been changed")
            window.destroy()
        else:
            mg.showwarning("Invalid Password", "Password must include: an uppercase letter, a lowercase "
                                               "letter, a number, "
                                               "a special character (!@_&) and between 8 and 20 characters")
    else:
        mg.showwarning("Passwords don't match", "Passwords don't match. Please try again")


def checkEmail(email, reemail, level, user, window):
    from isValid import validEmail, verifyEmail
    if email == reemail:
        if validEmail(email) == True:
            if verifyEmail(email) == True:
                SQLfunctions.changeEmail(level, user, email)
                mg.showinfo("Email Changed", "Email has been changed")
                window.destroy()
            else:
                mg.showwarning("Invalid Email", "The email you have entered is invalid")
        else:
            mg.showwarning("Invalid Email", "The email you have entered is invalid")
    else:
        mg.showwarning("Emails don't match", "Emails don't match. Please try again")

def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")

def changePassUI(user, password, level):
    win = Toplevel()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    newPassVar = tkinter.StringVar()
    rePassVar = tkinter.StringVar()

    win.title("Change Password")

    chaLabel = Label(win, text="Change Password", font=("Arial", 20))
    chaLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    newPassLabel = Label(win, text="New Password:", font=("Arial", 16))
    newPassLabel.place(relx=0.07, rely=0.3, relheight=0.13, relwidth=0.3)
    newPassBox = Entry(win, textvariable=newPassVar, font=('Arial', 12), show='•', width=27)
    newPassBox.place(relx=0.38, rely=0.34, relheight=0.06, relwidth=0.48)

    rePassLabel = Label(win, text="Re-Type Password:", font=("Arial", 14))
    rePassLabel.place(relx=0, rely=0.5, relheight=0.13, relwidth=0.4)
    rePassBox = Entry(win, textvariable=rePassVar, font=('Arial', 12), show='•', width=27)
    rePassBox.place(relx=0.38, rely=0.54, relheight=0.06, relwidth=0.48)

    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(win, image=showPassImg, command=lambda: togglePass(newPassBox))
    showPass.place(relx=0.87, rely=0.33, relheight=0.07, relwidth=0.1)

    showRePass = Button(win, image=showPassImg, command=lambda: togglePass(rePassBox))
    showRePass.place(relx=0.87, rely=0.53, relheight=0.07, relwidth=0.1)

    changeBut = Button(win, text="Change Password", font=("Arial", 16),
                       command=lambda: checkPassword(newPassVar.get(), rePassVar.get(), level, user, win))
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

    changeBut = Button(win, text="Change Email", font=("Arial", 16),
                       command=lambda: checkEmail(newEmailVar.get(), reEmailVar.get(), level, user, win))
    # Add command that runs a value checker and then runs the SQL to change the database
    changeBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    newEmailBox.focus()
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
    # changeEmailUI("test", "test")
    changePassUI("test", "test", "Amdin")