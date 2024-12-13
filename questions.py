from tkinter import *
from tkinter import messagebox as mg
import json
from SQLfunctions import checkType, getQuest, getLast, getAnsw, getAssignID, saveSub
import re
import datetime
import os
"""
Do next:
- Store the answers when the user clicks next
- Function so when submit is pressed, it stores answers in the database and begins the marking process
"""

class Questions():
    def __init__(self, teacherID, questionNum, assignName, studentID):
        self.teachID = teacherID
        self.questionNum = questionNum
        self.assignName = assignName
        self.studentID = studentID
        self.answers = {}

    def nextQ(self, win, answerEntry):
        answer = answerEntry.get("1.0", END).strip()
        self.save_answer(answer)
        self.questionNum += 1
        win.destroy()
        self.createWindow()

    def save_answer(self, answer):
        self.answers[self.questionNum] = answer

    def save_answers_to_file(self):
        name = re.sub(r'[<>:"/\\|?*]', '', self.assignName)
        with open(f"{name}_answers.json", "w") as file:
            json.dump(self.answers, file)

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

        if checkType(self.assignName, self.questionNum) == "Calculation":
            answerEntry = Text(win, font=("Arial", 14))
            answerEntry.place(relx=0.2, rely=0.171, relheight=0.06, relwidth=0.3)
            workingLabel = Label(win, text="Working:", font=("Arial", 20))
            workingLabel.place(relx=0.03, rely=0.25)
            workingEntry = Text(win, font=("Arial", 14))
            workingEntry.place(relx=0.2, rely=0.27, relheight=0.5, relwidth=0.75)
        else:
            answerEntry = Text(win, font=("Arial", 14))
            answerEntry.place(relx=0.2, rely=0.17, relheight=0.6, relwidth=0.75)

        questionLabel = Label(win, text=getQuest(self.questionNum, self.assignName), font=("Arial", 20))
        questionLabel.pack()

        if self.questionNum != getLast(self.assignName):
            nextButton = Button(win, text="Next", font=("Arial", 18), command=lambda: self.nextQ(win, answerEntry))
            nextButton.place(relx=0.45, rely=0.85, relheight=0.1, relwidth=0.15)
        elif self.questionNum == getLast(self.assignName):
            submitButton = Button(win, text="Submit", font=("Arial", 18), command=lambda: self.submit_answers(answerEntry, win))
            submitButton.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.15)

        answerEntry.focus()

        win.resizable(False, False)
        win.mainloop()

    def submit_answers(self, answerEntry, win):
        answer = answerEntry.get("1.0", END).strip()
        self.save_answer(answer)
        self.save_answers_to_file()
        win.destroy()
        marking = Marking(self.assignName, self.studentID)
        marking.create_window(self.answers)

class Marking():
    def __init__(self, assignName, studentID):
        self.assignName = assignName
        self.studentID = studentID
        self.questionNum = 1
        self.marks = []

    # add save to database

    def nextMark(self, win, marksEntry, answers):
        mark = marksEntry.get()
        if self.saveMark(mark):
            self.questionNum += 1
            win.destroy()
            self.create_window(answers)
        else:
            mg.showerror("Error", "Please enter a valid mark")

    def saveMark(self, mark):
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
        name = re.sub(r'[<>:"/\\|?*]', '', self.assignName)
        file_name = f"{name}_answers.json"

        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return data.get(str(self.questionNum), None)
        except Exception as e:
            mg.showerror("Error", f"Error: {e}")

    def submitMarks(self, win, marksEntry):
        if self.saveMark(marksEntry.get()):
            total_marks = sum(self.marks)
            mg.showinfo("Marks", f"Total Marks: {total_marks} out of {sum([getAnsw(self.assignName, i)[1] for i in range(1, getLast(self.assignName) + 1)])}")
            assign_id = getAssignID(self.assignName)
            date = datetime.date.today()
            saveSub(assign_id, self.studentID, date, total_marks)

            name = re.sub(r'[<>:"/\\|?*]', '', self.assignName)
            file_name = f"{name}_answers.json"
            if os.path.exists(file_name):
                os.remove(file_name)


            win.destroy()
            # delete assignment from list
            # open student view



    def create_window(self, answers):
        win = Tk()
        win.title("Marking")

        wWidth = 750
        wHeight = 500
        xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
        yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
        win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

        # answer, your answer, mark
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

        answer = self.getAnswers()

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

        if self.questionNum != getLast(self.assignName):
            nextButton = Button(frame, text="Next", font=("Arial", 16), command=lambda: self.nextMark(win, marksEntry, answers))
            nextButton.pack(pady=5)
        elif self.questionNum == getLast(self.assignName):
            submitButton = Button(frame, text="Submit", font=("Arial", 16), command=lambda: self.submitMarks(win, marksEntry))
            submitButton.pack(pady=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        win.resizable(False, False)
        win.mainloop()

if __name__ == "__main__":
    question = Questions(1, 1, "a00000001", 1)
    question.createWindow()
    # mark = Marking("a00000001")
    # mark.create_window({1: "5"})
    pass
