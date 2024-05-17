import tkinter
from tkinter import *
import registerGetVal
from isValid import *
from tkinter import messagebox

def checkVal(username, email, password, window):
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
        # Add to student or teacher database
        messagebox.showinfo("Account Registered", "Your account has been registered successfully!")
        window.destroy()
        # LOG THEM IN IMMEDIATELY

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
    window.geometry("500x400")
    window.title("Register Account")

    password_var = tkinter.StringVar()
    repassword_var = tkinter.StringVar()

    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(x=140, y=10)

    registerButton = Button(window, text="Register Account", command=lambda: registerGetVal.getVal(nameBox, userBox,
                                                                                                   emailBox, passBox,
                                                                                                   repassBox, c, o,
                                                                                                   window))
    registerButton.config(font=("Arial", 16))
    registerButton.place(x=100, y=335)

    backButton = Button(window, text="Back", command=lambda: back(window))
    backButton.config(font=("Arial", 16))
    backButton.place(x=300, y=335)

# Name label and text box
    nameLabel = Label(window, text="Full Name:")
    nameLabel.config(font=("Arial", 14))
    nameLabel.place(x=82, y=60)
    nameBox = Text(window, height=1, width=30)
    nameBox.place(x=185, y=65)

# Username label and text box
    userLabel = Label(window, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(x=82, y=93)
    userBox = Text(window, height=1, width=30)
    userBox.place(x=185, y=100)

# Email label and text box
    emailLabel = Label(window, text="Email Address:")
    emailLabel.config(font=("Arial", 14))
    emailLabel.place(x=45, y=130)
    emailBox = Text(window, height=1, width=30)
    emailBox.place(x=185, y=135)

# Password label and text box
    passLabel = Label(window, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(x=85, y=170)
    # Makes whatever is entered into bullet points
    passBox = Entry(window, textvariable=password_var, font=('Arial', 12), show='•', width=27)
    passBox.place(x=185, y=175)

# Re-type label and text box
    repassLabel = Label(window, text="Re-type Password:")
    repassLabel.config(font=("Arial", 14))
    repassLabel.place(x=15, y=210)
    repassBox = Entry(window, textvariable=repassword_var, font=('Arial', 12), show='•', width=27)
    repassBox.place(x=185, y=215)

# School label
    schoolLabel = Label(window, text="School:")
    schoolLabel.config(font=("Arial", 14))
    schoolLabel.place(x=110, y=250)

# Drop-down menu for school
    options = ["City of Stoke-on-Trent Sixth Form College", "School not listed"]
    c = StringVar()
    c.set("School name")
    schoolMenu = OptionMenu(window, c, *options)
    schoolMenu.place(x=182, y=250)


# Label for level
    levelLabel = Label(window, text="I am a:")
    levelLabel.config(font=("Arial", 14))
    levelLabel.place(x=115, y=290)

# Drop-down menu for level of account
    levelOpt = ["Teacher", "Student"]
    o = StringVar()
    o.set("Level")
    levelMenu = OptionMenu(window, o, *levelOpt)
    levelMenu.place(x=182, y=290)

# Show password buttons
    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(window, image=showPassImg, command=lambda: togglePass(passBox))
    showPass.place(x=440, y=171)

    showRePass = Button(window, image=showPassImg, command=lambda: togglePass(repassBox))
    showRePass.place(x=440, y=213)

    nameBox.focus()
    window.mainloop()
