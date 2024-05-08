from tkinter import *
from tkinter import messagebox
import isValid

def createBox():
    window = Tk()

    window.geometry("500x400")
    window.title("Register Account")

    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(x=140, y=25)

    registerButton = Button(window, text="Test_Register_Window ")
    registerButton.config(font=("Arial", 16))
    registerButton.place(x=130, y=325)

    emailLabel = Label(window, text="Email Address:")
    emailLabel.config(font=("Arial", 14))
    emailLabel.place(x=50, y=100)

    emailBox =


    window.mainloop()


createBox() #REMOVE THIS OR BIG PROBLEMS


"""
Add text boxes with titles
Run commands that verify data entered
"""