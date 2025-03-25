# imports tkinter for the UI
from tkinter import *
from tkinter import messagebox
# imports the SQLfunctions file to check the login credentials
import SQLfunctions
# imports the PIL imaging library to show the logo and show password button
from PIL import Image, ImageTk
# imports the studentView and adminView files to show the appropriate window
import studentView
import adminView
# imports the pyotp library to generate the OTP
import pyotp
# imports the processWindows file to send the email
from processWindows import sendEmailOTP

# Generate a key for the user
def generateKey():
    key = pyotp.random_base32()
    return key

# Generate the OTP for the user
def generateOTP(key):
    otp = pyotp.TOTP(key)
    return otp.now()

# Verifies the OTP that was entered
def verify(key, otp):
    totp = pyotp.TOTP(key)
    return totp.verify(otp, valid_window=1)

# Creates the window for the user to enter the OTP
def createWindow(check, logInWin):
    win = Toplevel()

    win.title("Two-Factor Authentication")

    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    key = generateKey()
    otp = generateOTP(key)
    sendEmailOTP(check, otp)

    titleLabel = Label(win, font=("Arial", 16), text="Two-Factor Authentication")
    titleLabel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    infoLabel = Label(win, font=("Arial", 12), text="Please enter the code sent to your email.\n If you did not receive the code, please check your spam folder.")
    infoLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.15)

    codeLabel = Label(win, font=("Arial", 16), text="Code:")
    codeLabel.place(relx=0.05, rely=0.45, relwidth=0.2, relheight=0.1)

    codeBox = Entry(win, font=("Arial", 12))
    codeBox.place(relx=0.22, rely=0.46, relwidth=0.65, relheight=0.09)

    def logIn(check, key, logInWin): # Logs in the user and shows the appropriate window (Admin or Student)
        if verify(key, codeBox.get()):
            if check[0] == "Student":
                win.destroy()
                logInWin.destroy()
                studentView.createStudent(check[1], check[2], check[3])
            elif check[0] == "Admin":
                win.destroy()
                logInWin.destroy()
                adminView.createView(check[2], check[3], check[1])
        else:
            messagebox.showwarning("Invalid Code", "The code you entered is invalid. Please try again.")

    def enter(event=None):
        logIn(check, key, logInWin) # Calls the logIn function

    verifyButton = Button(win, font=("Arial", 16), text="Verify", command=enter)
    verifyButton.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.15)

    reSendButton = Button(win, font=("Arial", 16), text="Resend Code", command=lambda: sendEmailOTP(check, otp))
    reSendButton.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.15)

    win.bind("<Return>", enter) # Calls the enter function when the enter key is pressed

    codeBox.focus()

    win.resizable(False, False)
    win.mainloop()

def logIn(username, password, win):
    # Gets the username entered in the log in window
    usernameVal = username.get("1.0", "end-1c").strip().lower()
    # Gets the password entered in the log in window
    passwordVal = password.get().strip()
    # Passes the values to the database and checks if the credentials are correct
    check = SQLfunctions.checkLogIn(usernameVal.lower(), passwordVal)
    # If the credentials are incorrect, show a warning message
    if check is None:
        messagebox.showwarning("Incorrect Login", "Incorrect username or password")
    else:
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

    password_variable = StringVar() # Variable to store the password

    # Creates a frame to place the logo
    frame = Frame(win, width=1, height=1)
    frame.pack()
    frame.place(relx=0.5, rely=0.175, anchor="center")

    # Loads the logo and resizes it
    img = Image.open("./Pictures/logo.png")
    img = img.resize((int(img.width * 0.3), int(img.height * 0.3)))
    img = ImageTk.PhotoImage(img)

    # Places the logo in the frame
    label = Label(frame, image=img)
    label.pack()

    # Title label
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

    # Username and password labels and boxes
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

    showPassImg = PhotoImage(file="./Pictures/showPassword.png")
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
