# imports tkinter for the UI
import tkinter
from tkinter import *
from tkinter import messagebox
# imports the SQLfunctions file to check the login credentials
import SQLfunctions
# imports the PIL imaging library to show the logo and show password button
from PIL import Image, ImageTk



def logIn(username, password, win):
    # Gets the username entered in the log in window
    usernameVal = username.get("1.0", "end-1c").strip()
    # Gets the password entered in the log in window
    passwordVal = password.get().strip()
    # Passes the values to the database and checks if the credentials are correct
    check = SQLfunctions.checkLogIn(usernameVal.lower(), passwordVal)
    # If the credentials are incorrect, show a warning message
    if check is None:
        messagebox.showwarning("Incorrect Login", "Incorrect username or password")
    else:
        # If the credentials are correct, show the two-factor authentication window
        from twoFactorAuth import createWindow
        createWindow(check, win)

def togglePass(passBox):
    # Shows/hides the password in the password box when the show password button is pressed
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")


def createLogIn():
    win = Tk()

    # Calculates the center of the screen and displays the window there
    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("The Physics Lab - Log In")

    password_variable = tkinter.StringVar() # Variable to store the password

    # Creates a frame to place the logo
    frame = Frame(win, width=1, height=1)
    frame.pack()
    frame.place(relx=0.5, rely=0.175, anchor="center")

    # Loads the logo and resizes it
    img = Image.open("Pictures\\logo.png")
    img = img.resize((int(img.width * 0.3), int(img.height * 0.3)))
    img = ImageTk.PhotoImage(img)

    # Places the logo in the frame
    label = Label(frame, image=img)
    label.pack()

    titleLabel = Label(win, text="Log In")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(relx=0.15, rely=0.275, relheight=0.1, relwidth=0.7)

    # Closes the application
    exitButton = Button(win, text="Exit", command=lambda: win.destroy())
    exitButton.config(font=("Arial", 16))
    exitButton.place(relx=0.55, rely=0.8, relheight=0.13, relwidth=0.15)

    # Runs when the enter key or the log in button is pressed
    def enter(event=None):
        logIn(userBox, passBox, win)

    # Log in button. Calls the enter function when pressed
    logButton = Button(win, text="Log In", command=enter)
    logButton.config(font=("Arial", 16))
    logButton.place(relx=0.28, rely=0.8, relheight=0.13, relwidth=0.2)

    userLabel = Label(win, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(relx=0.12, rely=0.4, relheight=0.13, relwidth=0.2)
    userBox = Text(win, height=1, width=30)
    userBox.place(relx=0.34, rely=0.44, relheight=0.06, relwidth=0.48)

    passLabel = Label(win, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(relx=0.12, rely=0.6, relheight=0.13, relwidth=0.2)
    # Stores the password in password_variable
    passBox = Entry(win, textvariable=password_variable, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.34, rely=0.64, relheight=0.06, relwidth=0.48)

    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    # Runs the togglePass function when the show password button is pressed
    showPass = Button(win, image=showPassImg, borderwidth=0, command=lambda: togglePass(passBox))
    showPass.place(relx=0.85, rely=0.63, relheight=0.07, relwidth=0.1)

    # Runs the enter function when the enter key is pressed
    win.bind("<Return>", enter)

    userBox.focus()
    win.resizable(False, False)
    win.mainloop()

if __name__ == "__main__":
    createLogIn()
    pass
