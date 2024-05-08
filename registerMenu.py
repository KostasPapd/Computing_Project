from tkinter import *
from tkinter import messagebox
import validateRegisterData

def getVal(userBox, emailBox, passBox, repassBox, c):
    username = userBox.get("1.0", "end-1c").strip()
    email = emailBox.get("1.0", "end-1c").strip()
    password = passBox.get("1.0", "end-1c").strip()
    repassword = repassBox.get("1.0", "end-1c").strip()
    school = c.get()
    if school == "School not listed":
        messagebox.showwarning("School not listed", "You can't create an account because your school isn't"
                                                    " registered to PROGRAM NAME. Please talk to a teacher if you want "
                                                    "to register with us")
        # ADD PROGRAM NAME
    else:
        if password != repassword:
            messagebox.showwarning("Passwords don't match", "Passwords don't match. Please try again")
        else:
            validateRegisterData.checkVal(username, email, password)
    # Strip gets rid of whitespace, 1.0 and end-1c is where the indexing starts and ends


def createBox():
    window = Tk()

    window.geometry("500x375")
    window.title("Register Account")

    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(x=140, y=25)

    registerButton = Button(window, text="Register Account", command=lambda: getVal(userBox, emailBox, passBox,
                                                                                          repassBox, c))
    registerButton.config(font=("Arial", 16))
    registerButton.place(x=150, y=310)

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
    passBox = Text(window, height=1, width=30)
    passBox.place(x=185, y=175)

# Re-type label and text box
    repassLabel = Label(window, text="Re-type Password:")
    repassLabel.config(font=("Arial", 14))
    repassLabel.place(x=15, y=210)
    repassBox = Text(window, height=1, width=30)
    repassBox.place(x=185, y=215)

# School label
    schoolLabel = Label(window, text="School:")
    schoolLabel.config(font=("Arial", 14))
    schoolLabel.place(x=110, y=250)

# Drop-down menu
    options = ["City of Stoke-on-Trent Sixth Form College", "School not listed"]
    c = StringVar()
    c.set("School name")
    schoolMenu = OptionMenu(window, c, *options)
    schoolMenu.place(x=182, y=250)

    userBox.focus()
    window.mainloop()


createBox()# REMOVE THIS OR BIG PROBLEMS


"""
Add text boxes with titles
Run commands that verify data entered
"""