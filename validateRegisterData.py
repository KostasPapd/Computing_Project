from tkinter import messagebox
from isValid import *

def checkVal(username, email, password):
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
        print("Approved")  # Remove this line after database is added
        # Add to database
        # Account registered window and then go to the main menu/log them in immediately
