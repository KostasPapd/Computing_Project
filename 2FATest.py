import pyotp
import qrcode
from tkinter import *
from PIL import Image, ImageTk

def createQR():
    key = "G3b7Q9LmX2N1aKp8R4T"

    uri = pyotp.totp.TOTP(key).provisioning_uri(
        name='Test',
        issuer_name='ThePhysicsLab')

    qrcode.make(uri).save("qr.png")

    pass


def createQRWindow():
    win = Toplevel()

    win.title("Two-Factor Authentication")

    wWidth = 500
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    frame = Frame(win, width=60, height=40)
    frame.pack()
    frame.place(relx=0.15, rely=0.25)

    img = Image.open("qr.png")
    img = img.resize((350, 350))
    img = ImageTk.PhotoImage(img)

    label = Label(frame, image=img)
    label.pack()

    win.resizable(False, False)
    win.mainloop()

def verifyCode():
    pass


if __name__ == "__main__":
    # createQR()
    createQRWindow()