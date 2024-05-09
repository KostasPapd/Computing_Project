from tkinter import messagebox
from isValid import *


def checkVal(name, username, email, password):
    if len(name) < 1 or len(username) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showwarning("Empty Field", "Please fill out all fields")
    else:
        if validateUsername(username) == False:
            # Add username verification
            messagebox.showwarning("Invalid Username", "This username is invalid or already taken")
        elif validEmail(email) == False:
            if verifyEmail(email) == False:
                messagebox.showwarning("Invalid email", "The email you have entered is invalid")
        elif validatePassword(password) == False:
            messagebox.showwarning("Invalid password", "Your password must include: an uppercase letter, a "
                                                       "lowercase letter, a number, a special character (!@_&) and more "
                                                       "than 8 characters")
        else:
            print("Approved")
