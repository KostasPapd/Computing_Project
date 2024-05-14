from tkinter import messagebox
from isValid import *
import createMainMenu


def checkVal(username, email, password, window, school, level):
    if validateUsername(username) == False:
        # Add username verification
        messagebox.showwarning("Invalid Username", "This username is invalid or already taken")
    elif validEmail(email) == False:
        messagebox.showwarning("Invalid email", "The email you have entered is invalid")
    elif verifyEmail(email) == False:
        messagebox.showwarning("Invalid email", "The email you have entered is invalid")
    elif validatePassword(password) == False:
        messagebox.showwarning("Invalid password", "Your password must include: an uppercase letter, a "
                                                   "lowercase letter, a number, a special character (!@_&) and more "
                                                   "than 8 characters")
    else:
        # Add to student or teacher database
        messagebox.showinfo("Account Registered", "Your account has been registered successfully!")
        window.destroy()
        createMainMenu.createMenu()  # OR LOGIN THEM IN IMMEDIATELY
