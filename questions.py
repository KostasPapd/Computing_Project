from tkinter import *
import json
from SQLfunctions import checkType, getQuest, getLast, getAnsw
import re
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

        win.resizable(False, False)
        win.mainloop()

    def submit_answers(self, answerEntry, win):
        answer = answerEntry.get("1.0", END).strip()
        self.save_answer(answer)
        self.save_answers_to_file()
        win.destroy()
        marking = Marking(self.assignName)
        marking.create_window(self.answers)

class Marking():
    def __init__(self, assignName):
        self.assignName = assignName

    # add save to database

    def create_window(self, answers):
        for questionNum, answer in answers.items():
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

            c_answer = getAnsw(self.assignName, questionNum)
            answerLabel = Label(frame, text=f"Correct Answer: {c_answer}", font=("Arial", 16), wraplength=700)
            answerLabel.pack(anchor="w", padx=10, pady=5)
            yourAnswerLabel = Label(frame, text=f"Your Answer: {answer}", font=("Arial", 16), wraplength=700)
            yourAnswerLabel.pack(anchor="w", padx=10, pady=5)
            marksLabel = Label(frame, text=f"Mark:", font=("Arial", 16))
            marksLabel.pack(anchor="w", padx=10, pady=5)
            marksEntry = Entry(frame, font=("Arial", 16))
            marksEntry.pack(anchor="w", padx=10, pady=5)

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
