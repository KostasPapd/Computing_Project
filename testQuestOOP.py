from tkinter import *
from tkinter import messagebox as mg
from tkinter import filedialog, ttk
import psycopg2
import os
from dotenv import load_dotenv
from SQLfunctions import checkType

class Questions():
    def __init__(self, teacherID, questionNum, assignID):
        self.teachID = teacherID
        self.questionNum = questionNum
        self.assignID = assignID

    def createWindow(self):
        win = Tk()
        win.title(f"Question {self.questionNum}")

        wWidth = 750
        wHeight = 500
        xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
        yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
        win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

        answerLabel = Label(win, text="Answer:", font=("Arial", 20))
        answerLabel.place(relx=0.05, rely=0.15)

        def open_file_dialog():
            filename = filedialog.askopenfilename()
            if filename:
                # Define the directory where you want to save the files
                save_directory = "uploaded_files/"
                if not os.path.exists(save_directory):
                    os.makedirs(save_directory)

                # Get the base name of the file
                base_filename = os.path.basename(filename)

                # Define the full path where the file will be saved
                save_path = os.path.join(save_directory, base_filename)

                # Copy the file to the save directory
                with open(filename, 'rb') as src_file:
                    with open(save_path, 'wb') as dest_file:
                        dest_file.write(src_file.read())

                return save_path
            return None

        if checkType(self.assignID, self.questionNum) == "Calculation":
            orLabel = Label(win, text="or", font=("Arial", 20))
            orLabel.place(relx=0.5, rely=0.15)
            answerButton = Button(win, text="Upload Answer", font=("Arial", 18), command=lambda: open_file_dialog())
            answerButton.place(relx=0.2, rely=0.14, relheight=0.1, relwidth=0.25)
            answerEntry = Text(win, font=("Arial", 14))
            # add_placeholder(answerEntry, "Enter your answer here... (show all working out)")
            answerEntry.place(relx=0.2, rely=0.3, relheight=0.4, relwidth=0.7)
        else:
            answerEntry = Text(win, font=("Arial", 14))
            #add_placeholder(answerEntry, "Enter your answer here...")
            answerEntry.place(relx=0.2, rely=0.17, relheight=0.6, relwidth=0.75)

        #data = pullQuestions(assignID, questionNum)
        #questionLabel = Label(win, text=data[0], font=("Arial", 20))
        #questionLabel.pack()

        win.resizable(False, False)
        win.mainloop()


def nextQuestion(self):
        self.questionNum += 1
        self.createWindow()

question = Questions(1, 1, 1)
question.createWindow()