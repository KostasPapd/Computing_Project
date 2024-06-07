# Demo on using notebook
# tutorials : https://www.pythontutorial.net/tkinter/tkinter-notebook/

import tkinter as tk
from tkinter import ttk, messagebox
import loginUI2
def frame1_objects(theFrame):
    welcomeLabel = ttk.Label(theFrame, text=" Using Notebook Demo ")
    welcomeLabel.config(font=("Courier", 10))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    # creating weight and height labels:
    userLabel = ttk.Label(theFrame, text="Enter user name ")
    userLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    passLabel = ttk.Label(theFrame, text="Enter new password")
    passLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    # creating text-boxes (entry boxes):
    userEntry = ttk.Entry(theFrame, width=30)
    userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    passEntry = ttk.Entry(theFrame, width=30)
    passEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")
    # creating the buttons:
    exitButton = ttk.Button(theFrame, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10)

# using a function from previous modules
    clearButton = ttk.Button(theFrame, text="Clear", width=12, command=lambda: loginUI2.clearboxes(theFrame,userEntry, passEntry))
    clearButton.grid(row=3, column=1, padx=10, pady=10)

    enterButton = ttk.Button(theFrame, text="Enter", width=12)
    # later we add command to call a function
    enterButton.grid(row=3, column=2, padx=10, pady=10)

def frame2_objects(theFrame):
    welcomeLabel = ttk.Label(theFrame, text=" Using Notebook Demo Frame 2 ")
    welcomeLabel.config(font=("Courier", 10))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    # creating weight and height labels:

    # creating the buttons:
    exitButton = ttk.Button(theFrame, text="Quit", width=12, command=quit)
    exitButton.grid(row=1, column=0, padx=10, pady=10)

    backButton = ttk.Button(theFrame, text="Back", width=12) # no command attached here
    backButton.grid(row=1, column=1, padx=10, pady=10)

    nextButton = ttk.Button(theFrame, text="Next", width=12) # no command attached here
    # later we add command to call a function
    nextButton.grid(row=1, column=2, padx=10, pady=10)

def frame3_objects(frame3):
    def show_selected_number():
        messagebox.showinfo(title='Result',message=selected_num.get())

# declare options
    selected_num = tk.StringVar()
    nums = (('first', '1'),
             ('second', '2'),
             ('third', '3'),
             ('fourth', '4'),
             ('fifth', '5'))

    # label
    label = ttk.Label(frame3, text="What's your choice?")
    label.grid(row = 0, column = 0, padx=5, pady=5)
    n = 1
    # radio buttons
    for size in nums:
        # show a radio buttons
        element = ttk.Radiobutton(frame3, text=size[0], value=size[1], variable=selected_num)
        element.grid(row=n , column= 0, padx=5, pady=5, sticky="W")
        # next row
        n += 1

    button = ttk.Button(frame3, text="Get choice", command=lambda: show_selected_number())
    button.grid(row = n + 1, column = 0, sticky="W", padx=5, pady=5)

def mainwindow():

    # create main window
    win = tk.Tk()
    win.geometry('450x250') # set the size of the window
    win.title('Demo on using Notebook')
    win.resizable(False, False) # make it fixed
    # create a notebook
    notebook = ttk.Notebook(win) # add notebook on teh window
    notebook.grid() # show it on the grid

    # setting up styles:
    s = ttk.Style()
    # Create style used by default for all Frames
    s.configure('TFrame', background='#d6e8c2') # default
    # Create a specific style
    s.configure('frame1.TFrame', background='#efcb96') # specific

    # create frames inside the notebook
    frame1 = ttk.Frame(notebook, style="frame1.TFrame") # takes a pecific style
    frame2 = ttk.Frame(notebook) # takes the default style
    frame3 = ttk.Frame(notebook) # takes the default style

    # Adding objects on each frame:
    frame1_objects(frame1)
    frame2_objects(frame2)
    frame3_objects(frame3)
# show frames on the main window
    frame1.grid(sticky= tk.NW)
    frame2.grid(sticky= tk.E)
    frame3.grid(sticky= tk.NS)

    # add frames to notebook
    notebook.add(frame1, text='new      ') # adding frame1
    notebook.add(frame2, text='delete   ') # adding frame2
    notebook.add(frame3, text='update   ') # adding frame3

    win.mainloop()


if __name__=="__main__":
    mainwindow()