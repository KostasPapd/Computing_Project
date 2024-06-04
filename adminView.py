from tkinter import *
import registerMenu

def testSendEmail(email):
    # https://automatetheboringstuff.com/2e/chapter18/
    # https://mailtrap.io/blog/python-send-email/
    pass


def exitMenu(win):
    win.destroy()


def createView():
    win = Tk()
    win.title("Admin view")
    win.geometry("500x500")

    exitButton = Button(win, text="Exit", command=lambda: exitMenu(win))
    exitButton.config(font=("Arial", 20))
    exitButton.place(relx=0.37, rely=0.6, relheight=0.11, relwidth=0.23)

    createButton = Button(win, text="Create Account", command=lambda: registerMenu.createBox())
    createButton.config(font=("Arial", 16))
    createButton.place(relx=0.17, rely=0.7, relheight=0.11, relwidth=0.4)



    win.attributes("-fullscreen", True)
    win.resizable(False, False)
    win.mainloop()

createView()
