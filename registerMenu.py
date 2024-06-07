import tkinter
from tkinter import *
from isValid import *
from tkinter import messagebox
from adminView import sendEmailCreate
import SQLfunctions

def checkVal(email, password, window, name):
    if validEmail(email) == False:
        messagebox.showwarning("Invalid email", "The email you have entered is invalid")
    elif SQLfunctions.checkEmail(email) == False:
        messagebox.showwarning("Email taken", "This email is already taken")
    elif verifyEmail(email) == False:
        messagebox.showwarning("Invalid email", "The email you have entered is invalid")
    elif validatePassword(password) == False:
        messagebox.showwarning("Invalid password", "Your password must include: an uppercase letter, a "
                                                   "lowercase letter, a number, a special character (!@_&) and "
                                                   "between 8 and 20 characters")
    else:
        SQLfunctions.registerAcc(email, password, name)
        sendEmailCreate(email, password, name)
        messagebox.showinfo("Account Created", "Account has been created and details have been sent to student")
        window.destroy()

def getVal(nameBox, emailBox, passBox, repassBox, window):
    # Strip gets rid of whitespace at the beginning or the end of the string
    # 1.0 and end-1c is where the indexing starts and ends
    name = nameBox.get("1.0", "end-1c")
    email = emailBox.get("1.0", "end-1c").strip()
    password = passBox.get().strip()
    repassword = repassBox.get().strip()

    if len(name) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showwarning("Empty Field", "Please fill out all fields")
    else:
        # Capitalises the first letter of the first name and surname for the database
        space = 0
        for i in range(len(name)):
            if name[i].isspace():
                space = i
        if len(name) < 5:
            messagebox.showwarning("Name too short", "Please enter your full name")
        else:
            name = name[0].capitalize() + name[1:space] + " " + name[space + 1].capitalize() + name[space + 2:]

        if password != repassword:
            messagebox.showwarning("Passwords don't match", "Passwords don't match. Please try again")
        else:
            checkVal(email, password, window, name)

def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")


def createBox():
    window = Toplevel()

    wWidth = 500
    wHeight = 350
    xCord = int((window.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((window.winfo_screenheight() / 2) - (wHeight / 2))
    window.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    window.resizable(False, False)

    window.title("Register Account")

    password_var = tkinter.StringVar()
    repassword_var = tkinter.StringVar()

    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(relx=0.27, rely=0.01, relheight=0.11, relwidth=0.5)

    registerButton = Button(window, text="Register Account", command=lambda: getVal(nameBox, emailBox, passBox,
                                                                                    repassBox, window))
    registerButton.config(font=("Arial", 16))
    registerButton.place(relx=0.12, rely=0.7, relheight=0.11, relwidth=0.4)

    exitButton = Button(window, text="Exit", command=lambda: window.destroy())
    exitButton.config(font=("Arial", 16))
    exitButton.place(relx=0.65, rely=0.7, relheight=0.11, relwidth=0.15)

# Name label and text box
    nameLabel = Label(window, text="Full Name:")
    nameLabel.config(font=("Arial", 14))
    nameLabel.place(relx=0.05, rely=0.125, relheight=0.11, relwidth=0.4)
    nameBox = Text(window, height=1, width=30)
    nameBox.place(relx=0.37, rely=0.16, relheight=0.06, relwidth=0.48)

# Email label and text box
    emailLabel = Label(window, text="Email Address:")
    emailLabel.config(font=("Arial", 14))
    emailLabel.place(relx=0.06, rely=0.255, relheight=0.1, relwidth=0.3)
    emailBox = Text(window, height=1, width=30)
    emailBox.place(relx=0.37, rely=0.28, relheight=0.06, relwidth=0.48)

# Password label and text box
    passLabel = Label(window, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(relx=0.15, rely=0.38, relheight=0.1, relwidth=0.2)
    # Makes whatever is entered into bullet points
    passBox = Entry(window, textvariable=password_var, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.37, rely=0.4, relheight=0.06, relwidth=0.48)

# Re-type label and text box
    repassLabel = Label(window, text="Re-type Password:")
    repassLabel.config(font=("Arial", 14))
    repassLabel.place(relx=0.022, rely=0.5, relheight=0.1, relwidth=0.32)
    repassBox = Entry(window, textvariable=repassword_var, font=('Arial', 12), show='•', width=27)
    repassBox.place(relx=0.37, rely=0.52, relheight=0.06, relwidth=0.48)


# Show password buttons
    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(window, image=showPassImg, command=lambda: togglePass(passBox))
    showPass.place(relx=0.87, rely=0.39, relheight=0.07, relwidth=0.1)

    showRePass = Button(window, image=showPassImg, command=lambda: togglePass(repassBox))
    showRePass.place(relx=0.87, rely=0.51, relheight=0.07, relwidth=0.1)

    nameBox.focus()
    window.mainloop()


if __name__ == "__main__":
    # Testing
    # createBox()
    pass
