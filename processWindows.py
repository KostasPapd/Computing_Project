"""
MAKE ASSIGNMENT TABLE THE ASSIGNMENT ID AND PUT THAT INTO ASSIGNMENTS TABLE SO I CAN SEARCH USING THE TITLE ID

The UI and many processes will go in here

Add:
Change Password - get value and validation
Change Email - get value and validation
"""

import tkinter
from tkinter import *
import smtplib
from tkinter import messagebox as mg
from tkinter import ttk
import SQLfunctions
import ssl
from email.message import EmailMessage
import random

def checkPassword(passw, repassw, level, user, window):
    from isValid import validatePassword
    if passw == repassw:
        if validatePassword(passw) == True:
            SQLfunctions.changePass(user, level, passw)
            mg.showinfo("Password Changed", "Password has been changed")
            window.destroy()
        else:
            mg.showwarning("Invalid Password", "Password must include: an uppercase letter, a lowercase "
                                               "letter, a number, "
                                               "a special character (!@_&) and between 8 and 20 characters")
    else:
        mg.showwarning("Passwords don't match", "Passwords don't match. Please try again")


def checkEmail(email, reemail, level, user, window):
    from isValid import validEmail, verifyEmail
    if email == reemail:
        if validEmail(email) == True:
            if verifyEmail(email) == True:
                SQLfunctions.changeEmail(level, user, email)
                mg.showinfo("Email Changed", "Email has been changed")
                window.destroy()
            else:
                mg.showwarning("Invalid Email", "The email you have entered is invalid")
        else:
            mg.showwarning("Invalid Email", "The email you have entered is invalid")
    else:
        mg.showwarning("Emails don't match", "Emails don't match. Please try again")

def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")

def changePassUI(user, password, level):
    win = Toplevel()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    newPassVar = tkinter.StringVar()
    rePassVar = tkinter.StringVar()

    win.title("Change Password")

    chaLabel = Label(win, text="Change Password", font=("Arial", 20))
    chaLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    newPassLabel = Label(win, text="New Password:", font=("Arial", 16))
    newPassLabel.place(relx=0.07, rely=0.3, relheight=0.13, relwidth=0.3)
    newPassBox = Entry(win, textvariable=newPassVar, font=('Arial', 12), show='•', width=27)
    newPassBox.place(relx=0.38, rely=0.34, relheight=0.06, relwidth=0.48)

    rePassLabel = Label(win, text="Re-Type Password:", font=("Arial", 14))
    rePassLabel.place(relx=0, rely=0.5, relheight=0.13, relwidth=0.4)
    rePassBox = Entry(win, textvariable=rePassVar, font=('Arial', 12), show='•', width=27)
    rePassBox.place(relx=0.38, rely=0.54, relheight=0.06, relwidth=0.48)

    showPassImg = PhotoImage(file="Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(win, image=showPassImg, borderwidth=0, command=lambda: togglePass(newPassBox))
    showPass.place(relx=0.87, rely=0.33, relheight=0.07, relwidth=0.1)

    showRePass = Button(win, image=showPassImg, borderwidth=0, command=lambda: togglePass(rePassBox))
    showRePass.place(relx=0.87, rely=0.53, relheight=0.07, relwidth=0.1)

    changeBut = Button(win, text="Change Password", font=("Arial", 16),
                       command=lambda: checkPassword(newPassVar.get(), rePassVar.get(), level, user, win))
    changeBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    newPassBox.focus()
    win.resizable(False, False)
    win.mainloop()


def changeEmailUI(user, level):
    win = Toplevel()

    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Change Email")

    chaLabel = Label(win, text="Change Email", font=("Arial", 20))
    chaLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    newEmailLabel = Label(win, text="New Email:", font=("Arial", 16))
    newEmailLabel.place(relx=0.09, rely=0.3, relheight=0.13, relwidth=0.3)
    newEmailVar = tkinter.StringVar()
    newEmailBox = Entry(win, textvariable=newEmailVar, font=('Arial', 12), width=27)
    newEmailBox.place(relx=0.4, rely=0.34, relheight=0.06, relwidth=0.48)

    reEmailLabel = Label(win, text="Re-Type Email:", font=("Arial", 14))
    reEmailLabel.place(relx=0.02, rely=0.5, relheight=0.13, relwidth=0.4)
    reEmailVar = tkinter.StringVar()
    reEmailBox = Entry(win, textvariable=reEmailVar, font=('Arial', 12), width=27)
    reEmailBox.place(relx=0.4, rely=0.54, relheight=0.06, relwidth=0.48)

    changeBut = Button(win, text="Change Email", font=("Arial", 16),
                       command=lambda: checkEmail(newEmailVar.get(), reEmailVar.get(), level, user, win))
    # Add command that runs a value checker and then runs the SQL to change the database
    changeBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    newEmailBox.focus()
    win.resizable(False, False)
    win.mainloop()

def sendEmailCreate(email, password, name):
    try:
        server = "smtp.gmail.com"
        port = 465
        email_s = "thephysicslab12@gmail.com"
        passw = "ihbi vcsv tgjr npmu"

        receiver = email

        subject = "Account Created"
        message = (f"Hello {name},\n\nYour teacher has created a Physics Lab account for you. "
                   f"Your details are below:\n\n"
                   f"Username: {email}\nPassword: {password}\n\n"
                   f"Make sure to log in and change your password to something more secure. "
                   f"Please keep this information safe and do not share it with anyone.")

        email_c = EmailMessage()
        email_c['From'] = email
        email_c['to'] = receiver
        email_c['Subject'] = subject
        email_c.set_content(message)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(server, port, context=context) as server:
            server.login(email_s, passw)
            server.sendmail(email_s, receiver, email_c.as_string())

    except Exception as e:
        mg.showwarning("Email not sent", f"An error occurred: {e}")

def stuListUI(t_ID, updated):
    win = Toplevel()

    wWidth = 600
    wHeight = 600
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Add Students")

    titleLabel = Label(win, text="Add Students", font=("Arial", 20))
    titleLabel.pack()

    scroll = Scrollbar(win)
    scroll.pack(side=RIGHT, fill=Y)

    students = SQLfunctions.getStudents(t_ID)
    stuList = Listbox(win, selectmode=MULTIPLE, width=35, height=20, borderwidth=0, bg='#f0f0f0', font="Arial 16",
                      yscrollcommand=scroll.set)

    if students is not None:
        students = sorted(students)
        for student in students:
            stuList.insert(END, student)
    stuList.pack(side=LEFT, fill=BOTH)

    selectedStu = []

    def select():
        nonlocal selectedStu
        selected = stuList.curselection()
        selectedStu = [stuList.get(n) for n in selected]
        updated(selectedStu)
        win.destroy()

    selectButton = Button(win, text="Select", font=("Arial", 18), command=select)
    selectButton.place(relx=0.75, rely=0.3, relheight=0.1, relwidth=0.2)

    cancelBut = Button(win, text="Cancel", font=("Arial", 18), command=lambda: win.destroy())
    cancelBut.place(relx=0.75, rely=0.5, relheight=0.1, relwidth=0.2)


    win.resizable(False, False)
    win.mainloop()


def createClassUI(t_ID):
    win = Toplevel()

    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Create Class")

    titleLabel = Label(win, text="Create Class", font=("Arial", 20))
    titleLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    nameLabel = Label(win, text="Class Name:", font=("Arial", 16))
    nameLabel.place(relx=0.06, rely=0.25, relheight=0.13, relwidth=0.3)
    nameVar = tkinter.StringVar()
    nameBox = Entry(win, textvariable=nameVar, font=('Arial', 12), width=27)
    nameBox.place(relx=0.35, rely=0.28, relheight=0.08, relwidth=0.55)

    students = []

    def update_students(selected_students):
        nonlocal students
        students = selected_students
    def addStu(t_ID):
        stuListUI(t_ID, update_students)

    stuLabel = Label(win, text="Students:", font=("Arial", 16))
    stuLabel.place(relx=0.09, rely=0.5, relheight=0.13, relwidth=0.3)
    stuButton = Button(win, text="Add Students", font=("Arial", 16), command=lambda: addStu(t_ID))
    stuButton.place(relx=0.35, rely=0.5, relheight=0.13, relwidth=0.3)

    def create_class():
        SQLfunctions.createClass(nameVar.get(), t_ID, students)
        win.destroy()

    createBut = Button(win, text="Create Class", font=("Arial", 16), command=create_class)
    createBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    win.resizable(False, False)
    win.mainloop()

def createAssignmentNumber():
    assignmentID = ""
    for i in range(8):
        assignmentID += str(random.randint(0, 9))
    if SQLfunctions.checkAssignmentNumber(assignmentID) == False:
        return assignmentID
    else:
        createAssignmentNumber()

def sendEmailOTP(check, otp):
    try:
        server = "smtp.gmail.com"
        port = 465
        # login for the email account
        email_s = "thephysicslab12@gmail.com"
        passw = "ihbi vcsv tgjr npmu"

        # selects the receiving email
        if check[0] == "Student":
            receiver = check[2]
        elif check[0] == "Admin":
            receiver = check[4]

        # email subject and message
        subject = "One-Time Password"
        message = f"Here is your one-time password: {otp}\n\n Do not share this code with anyone."

        # creates the email using the EmailMessage class from the email module
        email_c = EmailMessage()
        email_c['From'] = email_s
        email_c['to'] = receiver
        email_c['Subject'] = subject
        email_c.set_content(message)

        # creates a secure connection to the email server
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(server, port, context=context) as server:
            server.login(email_s, passw)
            server.sendmail(email_s, receiver, email_c.as_string())

    except Exception as e:
        # error handling
        mg.showwarning("Email not sent", f"An error occurred: {e}")

def deleteClassUI(teacher_id):
    win = Toplevel()

    wWidth = 600
    wHeight = 600
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Delete Class")

    titleLabel = Label(win, text="Delete Class", font=("Arial", 20))
    titleLabel.pack()

    scroll = Scrollbar(win)
    scroll.pack(side=RIGHT, fill=Y)

    classes = SQLfunctions.getClass(teacher_id)
    classList = Listbox(win, selectmode=MULTIPLE, width=35, height=20, borderwidth=0, bg='#f0f0f0', font="Arial 16",
                      yscrollcommand=scroll.set)

    if classes is not None:
        students = sorted(classes)
        for student in students:
            classList.insert(END, student)
    classList.pack(side=LEFT, fill=BOTH)

    selectedClass = []

    def delete(teacher_id):
        nonlocal selectedClass
        selected = classList.curselection()
        selectedClass = [classList.get(n) for n in selected]
        deleteClass = SQLfunctions.deleteClass(teacher_id, selectedClass)
        if deleteClass == True:
            mg.showinfo("Class Deleted", "The class has been deleted")
        else:
            mg.showwarning("Error", "An error occurred. Please try again")
        win.destroy()

    selectButton = Button(win, text="Delete", font=("Arial", 18), command=lambda: delete(teacher_id))
    selectButton.place(relx=0.75, rely=0.3, relheight=0.1, relwidth=0.2)

    cancelBut = Button(win, text="Cancel", font=("Arial", 18), command=lambda: win.destroy())
    cancelBut.place(relx=0.75, rely=0.5, relheight=0.1, relwidth=0.2)


    win.resizable(False, False)
    win.mainloop()

def assignmentObjects(frame, id):
    title = Label(frame, text="Assignments", font=("Arial", 20))
    title.pack()

    assignments = SQLfunctions.getAssignInfo(id)

    if assignments:
        columns = ("Assignment ID", "Title", "Due Date", "Class Name")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("Assignment ID", text="Assignment ID")
        tree.heading("Title", text="Title")
        tree.heading("Due Date", text="Due Date")
        tree.heading("Class Name", text="Class Name")

        tree.column("Assignment ID", width=50)
        tree.column("Title", width=150)
        tree.column("Due Date", width=60)
        tree.column("Class Name", width=150)

        for assignment in assignments:
            tree.insert("", "end", values=assignment)

        tree.pack(fill=BOTH, expand=True)

        def sort_by_column(tree, col, reverse):
            l = [(tree.set(k, col), k) for k in tree.get_children('')]
            l.sort(reverse=reverse)

            for index, (val, k) in enumerate(l):
                tree.move(k, '', index)

            tree.heading(col, command=lambda: sort_by_column(tree, col, not reverse))

        sort_by_id_button = Button(frame, text="Sort by Assignment ID",
                                   command=lambda: sort_by_column(tree, "Assignment ID", False))
        sort_by_id_button.pack(side=LEFT, padx=10, pady=10)

        sort_by_title_button = Button(frame, text="Sort by Title", command=lambda: sort_by_column(tree, "Title", False))
        sort_by_title_button.pack(side=LEFT, padx=10, pady=10)
    else:
        no_data_label = Label(frame, text="No assignments found.", font=("Arial", 16))
        no_data_label.pack()

def submissionObjects(frame, id):
    title = Label(frame, text="Submissions", font=("Arial", 20))
    title.pack()

    submissions = SQLfunctions.getSubmissions(id)

    if submissions:
        columns = ("Title", "Submission ID", "Student Name", "Mark", "Submission Date")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("Title", text="Assignment Title")
        tree.heading("Submission ID", text="Submission ID")
        tree.heading("Student Name", text="Student Name")
        tree.heading("Mark", text="Mark")
        tree.heading("Submission Date", text="Submission Date")

        tree.column("Title", width=150)
        tree.column("Submission ID", width=100)
        tree.column("Student Name", width=150)
        tree.column("Mark", width=50)
        tree.column("Submission Date", width=150)

        for submission in submissions:
            tree.insert("", "end", values=submission)

        tree.pack(fill=BOTH, expand=True)

        def sort_by_column(tree, col, reverse):
            l = [(tree.set(k, col), k) for k in tree.get_children('')]
            l.sort(reverse=reverse)

            for index, (val, k) in enumerate(l):
                tree.move(k, '', index)

            tree.heading(col, command=lambda: sort_by_column(tree, col, not reverse))

        sort_by_id_button = Button(frame, text="Sort by Submission ID", command=lambda: sort_by_column(tree, "Submission ID", False))
        sort_by_id_button.pack(side=LEFT, padx=10, pady=10)

        sort_by_title_button = Button(frame, text="Sort by Title", command=lambda: sort_by_column(tree, "Title", False))
        sort_by_title_button.pack(side=LEFT, padx=10, pady=10)
    else:
        no_data_label = Label(frame, text="No submissions found.", font=("Arial", 16))
        no_data_label.pack()

def submissionViewCreate(window, id):
    # window.destroy()

    win = Tk()

    wWidth = 600
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Assignments")

    notebook = ttk.Notebook(win)
    notebook.grid()

    assignments = Frame(notebook)
    submissions = Frame(notebook)

    assignmentObjects(assignments, id)
    submissionObjects(submissions, id)

    assignments.grid()
    submissions.grid()

    notebook.add(assignments, text="View Assignments")
    notebook.add(submissions, text="View Submissions")


    win.resizable(False, False)
    win.mainloop()

if __name__ == "__main__":
    # changeEmailUI("test", "test")
    # changePassUI("test", "test", "Admin")
    # createClassUI(1)
    # stuListUI(1)
    # createAssignmentNumber()
    # sendEmailOTP("kostispapd@outlook.com", "123456")
    # deleteClassUI(1)
    submissionViewCreate(1, 1)
    pass
