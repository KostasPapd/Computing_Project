import tkinter
from tkinter import *
import studentView
import adminView
import SQLfunctions
from tkinter import messagebox


def logIn(username, password, win):
    username = username.get("1.0", "end-1c").strip()  # Pass these value to check against the database
    password = password.get().strip()
    check = SQLfunctions.checkLogIn(username, password)  # Check if the login is correct
    if check is None:
        messagebox.showwarning("Incorrect Login", "Incorrect username or password")
    else:
        if check[0] == "Student":
            win.destroy()
            studentView.createStudent(check[1], check[2], check[3])
        elif check[0] == "Admin":
            win.destroy()
            adminView.createView(check[2], check[3], check[1])




def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")


def createLogIn():
    win = Tk()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("The Physics Lab - Log In")

    password_variable = tkinter.StringVar()

    # ADD WHEN LOGO IS DONE
    # frame = Frame(win, width=60, height=40)
    # frame.pack()
    # frame.place(x=90, y=50) # Change to rel pos

    # img = Image.open("iconNotPng.png")  # LOGO GOES HERE
    # img = img.resize((120, 120))
    # img = ImageTk.PhotoImage(img)

    # label = Label(frame, image=img)
    # label.pack()

    titleLabel = Label(win, text="Log In")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(relx=0.13, rely=0.05, relheight=0.1, relwidth=0.7)

    exitButton = Button(win, text="Exit", command=lambda: win.destroy())
    exitButton.config(font=("Arial", 16))
    exitButton.place(relx=0.55, rely=0.8, relheight=0.13, relwidth=0.15)

    logButton = Button(win, text="Log In", command=lambda: logIn(userBox, passBox, win))
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
    passBox = Entry(win, textvariable=password_variable, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.34, rely=0.64, relheight=0.06, relwidth=0.48)

    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(win, image=showPassImg, borderwidth=0, command=lambda: togglePass(passBox))
    showPass.place(relx=0.85, rely=0.63, relheight=0.07, relwidth=0.1)

    userBox.focus()
    win.resizable(False, False)
    win.mainloop()

if __name__ == "__main__":
    # Testing
    createLogIn()
    pass
