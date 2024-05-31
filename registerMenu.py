import tkinter
from tkinter import *
import registerGetVal
from isValid import *
from tkinter import messagebox
import studentView
import SQLfunctions

def checkVal(username, email, password, window, name, school, level):
    if validateUsername(username) == False:
        # Add username verification
        messagebox.showwarning("Invalid Username", "This username is invalid or already taken")
    elif validEmail(email) == False:
        messagebox.showwarning("Invalid email", "The email you have entered is invalid")
    elif verifyEmail(email) == False:
        messagebox.showwarning("Invalid email", "The email you have entered is invalid")
    elif validatePassword(password) == False:
        messagebox.showwarning("Invalid password", "Your password must include: an uppercase letter, a "
                                                   "lowercase letter, a number, a special character (!@_&) and "
                                                   "between 8 and 20 characters")
    else:
        SQLfunctions.registerAcc(username, email, password, name, school, level)
        messagebox.showinfo("Account Registered", "Your account has been registered successfully!")
        window.destroy()
        # studentView.createStudent(name)
        # LOG THEM IN IMMEDIATELY BY CREATING STUDENT VIEW AND PASSING USERNAME AND PASSWORD AS PARAMETERS

def back(win):
    import createMainMenu
    win.destroy()
    createMainMenu.createMenu()

def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")


def createBox():
    window = Tk()

    wWidth = 500
    wHeight = 400
    xCord = int((window.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((window.winfo_screenheight() / 2) - (wHeight / 2))
    window.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    window.title("Register Account")

    password_var = tkinter.StringVar()
    repassword_var = tkinter.StringVar()

    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    # Change to relative pos
    titleLabel.place(relx=0.27, rely=0.01, relheight=0.11, relwidth=0.5)

    registerButton = Button(window, text="Register Account", command=lambda: registerGetVal.getVal(nameBox, userBox,
                                                                                                   emailBox, passBox,
                                                                                                   repassBox, c, o,
                                                                                                   window))
    registerButton.config(font=("Arial", 16))
    registerButton.place(relx=0.17, rely=0.85, relheight=0.11, relwidth=0.4)

    backButton = Button(window, text="Back", command=lambda: back(window))
    backButton.config(font=("Arial", 16))
    backButton.place(relx=0.6, rely=0.85, relheight=0.11, relwidth=0.15)

# Name label and text box
    nameLabel = Label(window, text="Full Name:")
    nameLabel.config(font=("Arial", 14))
    nameLabel.place(relx=0.05, rely=0.125, relheight=0.11, relwidth=0.4)
    nameBox = Text(window, height=1, width=30)
    nameBox.place(relx=0.37, rely=0.16, relheight=0.06, relwidth=0.48)

# Username label and text box
    userLabel = Label(window, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(relx=0.145, rely=0.22, relheight=0.1, relwidth=0.2)
    userBox = Text(window, height=1, width=30)
    userBox.place(relx=0.37, rely=0.25, relheight=0.06, relwidth=0.48)

# Email label and text box
    emailLabel = Label(window, text="Email Address:")
    emailLabel.config(font=("Arial", 14))
    emailLabel.place(relx=0.06, rely=0.315, relheight=0.1, relwidth=0.3)
    emailBox = Text(window, height=1, width=30)
    emailBox.place(relx=0.37, rely=0.34, relheight=0.06, relwidth=0.48)

# Password label and text box
    passLabel = Label(window, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(relx=0.15, rely=0.415, relheight=0.1, relwidth=0.2)
    # Makes whatever is entered into bullet points
    passBox = Entry(window, textvariable=password_var, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.37, rely=0.44, relheight=0.06, relwidth=0.48)

# Re-type label and text box
    repassLabel = Label(window, text="Re-type Password:")
    repassLabel.config(font=("Arial", 14))
    repassLabel.place(relx=0.022, rely=0.515, relheight=0.1, relwidth=0.32)
    repassBox = Entry(window, textvariable=repassword_var, font=('Arial', 12), show='•', width=27)
    repassBox.place(relx=0.37, rely=0.54, relheight=0.06, relwidth=0.48)

# School label
    schoolLabel = Label(window, text="School:")
    schoolLabel.config(font=("Arial", 14))
    schoolLabel.place(relx=0.18, rely=0.61, relheight=0.1, relwidth=0.2)

# Drop-down menu for school
    options = ["City of Stoke-on-Trent Sixth Form College", "School not listed"]
    c = StringVar()
    c.set("School name")
    schoolMenu = OptionMenu(window, c, *options)
    schoolMenu.place(relx=0.36, rely=0.62, relheight=0.08, relwidth=0.22)


# Label for level
    levelLabel = Label(window, text="I am a:")
    levelLabel.config(font=("Arial", 14))
    levelLabel.place(relx=0.21, rely=0.72, relheight=0.08, relwidth=0.15)

# Drop-down menu for level of account
    levelOpt = ["Teacher", "Student"]
    o = StringVar()
    o.set("Level")
    levelMenu = OptionMenu(window, o, *levelOpt)
    levelMenu.place(relx=0.36, rely=0.72, relheight=0.08, relwidth=0.15)

# Show password buttons
    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(window, image=showPassImg, command=lambda: togglePass(passBox))
    showPass.place(relx=0.87, rely=0.43, relheight=0.07, relwidth=0.1)

    showRePass = Button(window, image=showPassImg, command=lambda: togglePass(repassBox))
    showRePass.place(relx=0.87, rely=0.53, relheight=0.07, relwidth=0.1)

    nameBox.focus()
    window.resizable(False, False)
    window.mainloop()
