"""
- When loging in
    - Generate key and OTP
    - Send email with OTP
    - Create window to ask for password
    - Log in once OTP is correct

"""

import pyotp
from tkinter import messagebox as mg
from tkinter import *
from processWindows import sendEmailOTP

def generateKey():
    key = pyotp.random_base32()
    return key

def generateOTP(key):
    otp = pyotp.TOTP(key)
    return otp.now()

def verify(key, otp):
    totp = pyotp.TOTP(key)
    if totp.verify(otp, valid_window=1):
        print("Correct") # CHANGE TO LOG YOU IN
    else:
        mg.showwarning("Incorrect OTP", "The OTP entered is incorrect. Please try again.")

def createWindow(email):
    win = Toplevel()

    win.title("Two-Factor Authentication")

    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    key = generateKey()
    otp = generateOTP(key)
    sendEmailOTP(email, otp)

    titleLabel = Label(win, font=("Arial", 16), text="Two-Factor Authentication")
    titleLabel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    infoLabel = Label(win, font=("Arial", 12), text="Please enter the code sent to your email.\n If you did not receive the code, please check your spam folder.")
    infoLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.15)

    codeLabel = Label(win, font=("Arial", 16), text="Code:")
    codeLabel.place(relx=0.05, rely=0.45, relwidth=0.2, relheight=0.1)

    codeBox = Entry(win, font=("Arial", 12))
    codeBox.place(relx=0.22, rely=0.46, relwidth=0.65, relheight=0.09)

    verifyButton = Button(win, font=("Arial", 16), text="Verify", command=lambda: verify(key, codeBox.get()))
    verifyButton.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.15)

    reSendButton = Button(win, font=("Arial", 16), text="Resend Code", command=lambda: sendEmailOTP(email, otp))
    reSendButton.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.15)

    codeBox.focus()

    win.resizable(False, False)
    win.mainloop()

if __name__ == "__main__":
    createWindow("sokihay381@iminko.com")
    pass
