from tkinter import *
from tkinter import font as regFont
import isValid

def createBox():
    window = Tk()

    window.geometry("400x300")
    window.title("Register Account")

    text = regFont.Font(font="Arial", size=36)
    registerButton = Button(text="Register", font=text)
    registerButton.grid(row=10, column=10, pady=200, padx=154, sticky="NW")

    window.mainloop()

createBox()

"""
Add text boxes with titles
Run commands that verify data entered
"""