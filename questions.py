from tkinter import *
from tkinter import filedialog
import os
from SQLfunctions import checkType, getQuest, getLast

"""
Do next:
- Store the answers when the user clicks next
- Function so when submit is pressed, it stores answers in the database and begins the marking process
"""

class Questions():
    def __init__(self, teacherID, questionNum, assignName):
        self.teachID = teacherID
        self.questionNum = questionNum
        self.assignName = assignName

    def nextQ(self, win):
        self.questionNum += 1
        win.destroy()
        self.createWindow()

    def back(self, win):
        self.questionNum -= 1
        win.destroy()
        self.createWindow()

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

        if checkType(self.assignName, self.questionNum) == "Calculation":
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

        questionLabel = Label(win, text=getQuest(self.questionNum, self.assignName), font=("Arial", 20))
        questionLabel.pack()


        if self.questionNum > 1:
            backButton = Button(win, text="Back", font=("Arial", 18), command=lambda: self.back(win))
            backButton.place(relx = 0.3, rely = 0.85, relheight = 0.1, relwidth = 0.15)

        if self.questionNum != getLast(self.assignName):
            nextButton = Button(win, text="Next", font=("Arial", 18), command=lambda: self.nextQ(win))
            nextButton.place(relx = 0.6, rely = 0.85, relheight = 0.1, relwidth = 0.15)
        elif self.questionNum == getLast(self.assignName):
            submitButton = Button(win, text="Submit", font=("Arial", 18))
            submitButton.place(relx = 0.6, rely = 0.85, relheight = 0.1, relwidth = 0.15)


        win.resizable(False, False)
        win.mainloop()

if __name__ == "__main__":
    question = Questions(1, 1, "a00000001")
    question.createWindow()
