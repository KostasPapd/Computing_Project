from tkinter import *


# here we will find tkinter code that creates the login window.
# user enters username and password, and can click either:
# 1. Clear boxes to clear the boxes and start again
# 2. Exit button to exit.
# 3. Enter button to take the details and process them (runs get_login()).



# this function will extract the username and password from entry boxes
# then pass them for processing
def get_login(win, username, passward):

    userVar = username.get()
    passVar = passward.get()



def clearboxes(win, b1, b2):
    b1.delete(0, 'end')
    b2.delete(0, 'end')
    b1.focus()

# only tkinter work for login
def mainwindow():
    form = Tk()
    form.title("Welcome to login mini project demo")
    form.geometry("500x220")
    # creating welcome label:
    welcomeLabel = Label(form, text=" Welcome to my login")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    # creating weight and height labels:
    userLabel = Label(form, text="User name")
    userLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    passLabel = Label(form, text="Password")
    passLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    helpLabel = Label(form, text=" Enter username and password")
    helpLabel.grid(row=1, rowspan=2, column=2, padx=10, pady=10)
    # creating text-boxes (entry boxes):
    userEntry = Entry(form, width="30")
    userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
    passEntry = Entry(form, width="30", show='*')# Show * to hide the password
    passEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")
    # creating the buttons:
    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10)

    enterButton = Button(form, text="Clear", width=12, command=lambda: clearboxes(form,userEntry, passEntry))
    enterButton.grid(row=3, column=1, padx=10, pady=10)

    enterButton = Button(form, text="Enter", width=12, command=lambda: get_login(form, userEntry,passEntry))
    # later we add command to call a function
    enterButton.grid(row=3, column=2, padx=10, pady=10)

    userEntry.focus()  # set the focus to eightEntry box (the top one)
    # makes it easy to user to avoid clicking the box before
    # we enter the data
    form.eval('tk::PlaceWindow . center')  # centres the window on the screen
    mainloop()



if __name__ == "__main__": # for testing
    mainwindow()