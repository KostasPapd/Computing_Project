from tkinter import *
from tkinter import messagebox as mg
import json
from SQLfunctions import checkType, getQuest, getLast, getAnsw, getAssignID, saveSub, getName
import re
import datetime
import os

class Questions():
    def __init__(self, teacherID, questionNum, assignName, studentID, password):
        # constructor
        self.teachID = teacherID
        self.questionNum = questionNum
        self.assignName = assignName.strip('"')
        self.studentID = studentID
        self.password = password
        self.answers = {}

    def prevQ(self, win, answerEntry):
        # goes to previous question
        answer = answerEntry.get("1.0", END).strip()
        self.save_answer(answer)
        self.questionNum -= 1
        win.destroy()
        self.createWindow()

    def nextQ(self, win, answerEntry):
        # goes to next question
        if len(answerEntry.get("1.0", END).strip()) == 0: # checks if answer is empty
            mg.showerror("Error", "Please enter an answer")
        else:
            answer = answerEntry.get("1.0", END).strip()
            self.save_answer(answer)
            self.questionNum += 1
            win.destroy()
            self.createWindow()

    def save_answer(self, answer):
        # saves the answer to the dictionary
        self.answers[self.questionNum] = answer

    def save_answers_to_file(self):
        # saves the answers to a json file
        name = re.sub(r'[<>:"/\\|?*]', '', self.assignName)
        with open(f"{name}_answers.json", "w") as file:
            json.dump(self.answers, file)

    def createWindow(self):
        # creates the window for the questions
        win = Tk() # window instance
        win.title(f"Question {self.questionNum}")
        # sets the window size and position
        wWidth = 750
        wHeight = 500
        xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
        yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
        win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

        answerLabel = Label(win, text="Answer:", font=("Arial", 20))
        answerLabel.place(relx=0.05, rely=0.15)

        previous_answer = self.answers.get(self.questionNum, "") # Get the previous answer if it exists

        if checkType(self.assignName, self.questionNum) == "Calculation": # if the question is a calculation
            answerEntry = Text(win, font=("Arial", 14))
            answerEntry.place(relx=0.2, rely=0.171, relheight=0.06, relwidth=0.3)
            answerEntry.insert(END, previous_answer)
            workingLabel = Label(win, text="Working:", font=("Arial", 20))
            workingLabel.place(relx=0.03, rely=0.25)
            workingEntry = Text(win, font=("Arial", 14))
            workingEntry.place(relx=0.2, rely=0.27, relheight=0.5, relwidth=0.75)
        else: # if the question is a text answer
            answerEntry = Text(win, font=("Arial", 14))
            answerEntry.place(relx=0.2, rely=0.17, relheight=0.6, relwidth=0.75)
            answerEntry.insert(END, previous_answer)

        questionLabel = Label(win, text=getQuest(self.questionNum, self.assignName), font=("Arial", 20))
        questionLabel.pack()

        if self.questionNum != getLast(self.assignName): # if not the last question
            nextButton = Button(win, text="Next", font=("Arial", 18), command=lambda: self.nextQ(win, answerEntry))
            nextButton.place(relx=0.45, rely=0.85, relheight=0.1, relwidth=0.15)
        elif self.questionNum == getLast(self.assignName): # if the last question
            submitButton = Button(win, text="Submit", font=("Arial", 18), command=lambda: self.submit_answers(answerEntry, win))
            submitButton.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.15)

        if self.questionNum != 1: # if not the first question
            prevButton = Button(win, text="Previous", font=("Arial", 18), command=lambda: self.prevQ(win, answerEntry))
            prevButton.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.15)

        answerEntry.focus()
        win.resizable(False, False)
        win.mainloop()

    def submit_answers(self, answerEntry, win):
        # submits the answers
        if len(answerEntry.get("1.0", END).strip()) == 0:
            mg.showerror("Error", "Please enter an answer")
        else:
            answer = answerEntry.get("1.0", END).strip()
            self.save_answer(answer)
            self.save_answers_to_file()
            win.destroy()
            marking = Marking(self.assignName, self.studentID, self.password)
            marking.create_window(self.answers)

class Marking():
    def __init__(self, assignName, studentID, password):
        # constructor
        self.assignName = assignName
        self.studentID = studentID
        self.password = password
        self.questionNum = 1
        self.marks = []

    def nextMark(self, win, marksEntry, answers):
        # mark the next question
        mark = marksEntry.get()
        if self.saveMark(mark):
            self.questionNum += 1
            win.destroy()
            self.create_window(answers)
        else:
            mg.showerror("Error", "Please enter a valid mark")

    def saveMark(self, mark):
        # saves the mark to the list
        try:
            mark = int(mark)
            if mark >= 0 and mark <= getAnsw(self.assignName, self.questionNum)[1]:
                self.marks.append(mark)
                return True
            else:
                return False
        except ValueError:
            return False

    def getAnswers(self):
        # gets answers from json file
        name = re.sub(r'[<>:"/\\|?*]', '', self.assignName)
        file_name = f"{name}_answers.json"

        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return data.get(str(self.questionNum), None)
        except Exception as e:
            mg.showerror("Error", f"Error: {e}")

    def submitMarks(self, win, marksEntry):
        # submits the marks to the database
        if self.saveMark(marksEntry.get()):
            total_marks = sum(self.marks)
            mg.showinfo("Marks", f"Total Marks: {total_marks} out of {sum([getAnsw(self.assignName, i)[1] for i in range(1, getLast(self.assignName) + 1)])}")
            assign_id = getAssignID(f"\"{self.assignName}\"")
            date = datetime.date.today()
            saveSub(assign_id, self.studentID, date, total_marks)

            name = re.sub(r'[<>:"/\\|?*]', '', self.assignName)
            file_name = f"{name}_answers.json"
            if os.path.exists(file_name):
                os.remove(file_name)

            self.endMarking(win)
        else:
            mg.showerror("Error", "Please enter a valid mark")

    def endMarking(self, win):
        # finishes the marking process
        from studentView import createStudent
        win.destroy()
        createStudent(getName(self.studentID), self.studentID, self.password)

    def create_window(self, answers):
        # creates the window for marking
        win = Tk()
        win.title("Marking")
        # sets the window size and position
        wWidth = 750
        wHeight = 500
        xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
        yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
        win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
        # scrollable canvas
        canvas = Canvas(win)
        scrollbar = Scrollbar(win, orient="vertical", command=canvas.yview)
        frame = Frame(canvas)

        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        question_info = getAnsw(self.assignName, self.questionNum)
        c_answer = question_info[0]
        mark = question_info[1]

        answer = self.getAnswers() # Get the answer from the JSON file

        answerLabel = Label(frame, text=f"Correct Answer: {c_answer}", font=("Arial", 16), wraplength=700)
        answerLabel.pack(anchor="w", padx=10, pady=5)

        yourAnswerLabel = Label(frame, text=f"Your Answer: {answer}", font=("Arial", 16), wraplength=700)
        yourAnswerLabel.pack(anchor="w", padx=10, pady=5)

        marksFrame = Frame(frame)
        marksFrame.pack(anchor="w", padx=10, pady=5)

        marksLabel = Label(marksFrame, text="Mark:", font=("Arial", 16))
        marksLabel.pack(side="left")

        marksEntry = Entry(marksFrame, font=("Arial", 16))
        marksEntry.pack(side="left", padx=5)

        marksTextLabel = Label(marksFrame, text=f"out of {mark}", font=("Arial", 16))
        marksTextLabel.pack(side="left")

        if self.questionNum != getLast(self.assignName): # if not the last question
            nextButton = Button(frame, text="Next", font=("Arial", 16), command=lambda: self.nextMark(win, marksEntry, answers))
            nextButton.pack(pady=5)
        elif self.questionNum == getLast(self.assignName): # if the last question
            submitButton = Button(frame, text="Submit", font=("Arial", 16), command=lambda: self.submitMarks(win, marksEntry))
            submitButton.pack(pady=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        marksEntry.focus()
        win.resizable(False, False)
        win.mainloop()

if __name__ == "__main__":
    question = Questions(1, 1, "a00000001", 3, "hdb")
    question.createWindow()
    # mark = Marking("a00000001")
    # mark.create_window({1: "5"})
    pass
