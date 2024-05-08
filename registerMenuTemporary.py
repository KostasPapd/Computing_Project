from tkinter import *

import isValid

def createBox():
    window = Tk()

    window.geometry("400x300")
    window.title("Register Account")

    registerButton = Button(window, text="Register")
    registerButton.config(font=("Arial", 36))
    registerButton.grid(row=10, column=10, pady=200, padx=154, sticky="NW")

    window.mainloop()

createBox()

"""
Add text boxes with titles
Run commands that verify data entered
"""