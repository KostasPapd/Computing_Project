from tkinter import *
#from tkinter import messagebox

def checkVal():
    print("Test")

def createBox():
    window = Tk()

    window.geometry("500x400")
    window.title("Register Account")

    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(x=140, y=25)

    registerButton = Button(window, text="Test_Register_Window", command=lambda: checkVal())
    registerButton.config(font=("Arial", 16))
    registerButton.place(x=130, y=325)

# Username label and text box
    userLabel = Label(window, text="Username:")
    userLabel.config(font=("Arial", 14))
    userLabel.place(x=60, y=93)
    userBox = Text(window, height=1, width=30)
    userBox.place(x=175, y=100)

# Email label and text box
    emailLabel = Label(window, text="Email Address:")
    emailLabel.config(font=("Arial", 14))
    emailLabel.place(x=21, y=130)
    emailBox = Text(window, height=1, width=30)
    emailBox.place(x=175, y=135)

    userBox.focus()
    window.mainloop()


createBox() #REMOVE THIS OR BIG PROBLEMS


"""
Add text boxes with titles
Run commands that verify data entered
"""