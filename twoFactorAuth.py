"""
- When called from logIn.py, this file will:
    - Generate a key and OTP
    - Send an email with OTP
    - Create window to ask for OTP
    - Log in once OTP is correct
"""
# imports the pyotp library to generate the OTP
import pyotp
# imports the tkinter library to create the UI
from tkinter import *
# imports the processWindows file to send the email
from processWindows import sendEmailOTP
# imports the studentView and adminView files to show the appropriate window
import studentView
import adminView

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

if __name__ == "__main__":
    pass
