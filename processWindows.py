import tkinter
from tkinter import *
import smtplib
from tkinter import messagebox as mg
from tkinter import filedialog, ttk
import SQLfunctions
import ssl
from email.message import EmailMessage
import random
from tkcalendar import Calendar
import datetime
from isValid import *

def checkPassword(passw, repassw, level, user, window):
    from isValid import validatePassword # imports the validatePassword function from the isValid module
    if passw == repassw: # checks if passwords match
        if validatePassword(passw) == True: # validates the password
            SQLfunctions.changePass(user, level, passw) # changes the password in the database
            mg.showinfo("Password Changed", "Password has been changed")
            window.destroy()
    # error handling
        else:
            mg.showwarning("Invalid Password", "Password must include: an uppercase letter, a lowercase "
                                               "letter, a number, "
                                               "a special character (!@_&) and between 8 and 20 characters")
    else:
        mg.showwarning("Passwords don't match", "Passwords don't match. Please try again")


def checkEmail(email, reemail, level, user, window):
    from isValid import validEmail, verifyEmail
    if email == reemail: # checks if emails match
        if validEmail(email) == True: # validates email
            if verifyEmail(email) == True: # verifies email
                SQLfunctions.changeEmail(level, user, email) # changes email in database
                mg.showinfo("Email Changed", "Email has been changed")
                window.destroy()
    # error handling
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

def changePassUI(user, level):
    win = Toplevel() # creates a new window

    # sets the window size and position
    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # creates StringVar instances for the password and re-entered password
    newPassVar = tkinter.StringVar()
    rePassVar = tkinter.StringVar()

    # title
    win.title("Change Password")

    # labels and buttons
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

    showPassImg = PhotoImage(file="./Pictures/showPassword.png")
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
    win = Toplevel() # creates a new window

    # sets the window size and position
    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # window title
    win.title("Change Email")

    # labels and buttons defined and placed
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
    changeBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    newEmailBox.focus()
    win.resizable(False, False)
    win.mainloop()

def sendEmailCreate(email, password, name):
    try:
        server = "smtp.gmail.com" # email server
        port = 465 # email port
        # login for the email account
        email_s = "thephysicslab12@gmail.com"
        passw = "ihbi vcsv tgjr npmu"

        receiver = email # receiving email (student email)

        # email subject and body
        subject = "Account Created"
        message = (f"Hello {name},\n\nYour teacher has created a Physics Lab account for you. "
                   f"Your details are below:\n\n"
                   f"Username: {email}\nPassword: {password}\n\n"
                   f"Make sure to log in and change your password to something more secure. "
                   f"Please keep this information safe and do not share it with anyone.")

        # creates the email using the EmailMessage class from the email module
        email_c = EmailMessage()
        email_c['From'] = email
        email_c['to'] = receiver
        email_c['Subject'] = subject
        email_c.set_content(message)

        # creates a secure connection to the email server
        context = ssl.create_default_context()
        # sends email
        with smtplib.SMTP_SSL(server, port, context=context) as server:
            server.login(email_s, passw)
            server.sendmail(email_s, receiver, email_c.as_string())

    # error handling
    except Exception as e:
        mg.showwarning("Email not sent", f"An error occurred: {e}")

def stuListUI(t_ID, updated):
    win = Toplevel() # window instance

    # sets the window size and position
    wWidth = 600
    wHeight = 600
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # wim title
    win.title("Add Students")

    titleLabel = Label(win, text="Add Students", font=("Arial", 20))
    titleLabel.pack()

    scroll = Scrollbar(win)
    scroll.pack(side=RIGHT, fill=Y)

    # gets all students under a certain teacher
    students = SQLfunctions.getStudents(t_ID)
    stuList = Listbox(win, selectmode=MULTIPLE, width=35, height=20, borderwidth=0, bg='#f0f0f0', font="Arial 16",
                      yscrollcommand=scroll.set)

    # puts students in alphabetical list
    if students is not None:
        students = sorted(students)
        for student in students:
            stuList.insert(END, student)
    stuList.pack(side=LEFT, fill=BOTH)

    # defines empty list of selected students
    selectedStu = []

    # returns the selected students to the main window
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
    win = Toplevel() # window instance

    # sets the window size and position
    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # window title
    win.title("Create Class")

    titleLabel = Label(win, text="Create Class", font=("Arial", 20))
    titleLabel.place(relx=0.26, rely=0.05, relheight=0.1, relwidth=0.5)

    nameLabel = Label(win, text="Class Name:", font=("Arial", 16))
    nameLabel.place(relx=0.06, rely=0.25, relheight=0.13, relwidth=0.3)
    nameVar = tkinter.StringVar()
    nameBox = Entry(win, textvariable=nameVar, font=('Arial', 12), width=27)
    nameBox.place(relx=0.35, rely=0.28, relheight=0.08, relwidth=0.55)

    # defines empty list of students
    students = []

    # function to add students to the list
    def update_students(selected_students):
        nonlocal students
        students = selected_students
    def addStu(t_ID):
        stuListUI(t_ID, update_students)

    stuLabel = Label(win, text="Students:", font=("Arial", 16))
    stuLabel.place(relx=0.09, rely=0.5, relheight=0.13, relwidth=0.3)
    stuButton = Button(win, text="Add Students", font=("Arial", 16), command=lambda: addStu(t_ID))
    stuButton.place(relx=0.35, rely=0.5, relheight=0.13, relwidth=0.3)

    # function to create class
    def create_class():
        if len(nameVar.get()) == 0 or len(students) == 0:
            mg.showwarning("Error", "Please fill in all fields")
        else:
            SQLfunctions.createClass(nameVar.get(), t_ID, students)
            win.destroy()

    createBut = Button(win, text="Create Class", font=("Arial", 16), command=create_class)
    createBut.place(relx=0.15, rely=0.75, relheight=0.13, relwidth=0.4)

    cancelBut = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelBut.place(relx=0.6, rely=0.75, relheight=0.13, relwidth=0.2)

    nameBox.focus()
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
    win = Toplevel() # window instance

    # sets the window size and position
    wWidth = 600
    wHeight = 600
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # title of window
    win.title("Delete Class")

    titleLabel = Label(win, text="Delete Class", font=("Arial", 20))
    titleLabel.pack()

    scroll = Scrollbar(win)
    scroll.pack(side=RIGHT, fill=Y)

    # gets all classes under a certain teacher
    classes = SQLfunctions.getClass(teacher_id)
    classList = Listbox(win, selectmode=MULTIPLE, width=35, height=20, borderwidth=0, bg='#f0f0f0', font="Arial 16",
                      yscrollcommand=scroll.set)

    # sorts classes alphabetically and adds them to list
    if classes is not None:
        students = sorted(classes)
        for student in students:
            classList.insert(END, student)
    classList.pack(side=LEFT, fill=BOTH)

    # defines empty list of selected classes
    selectedClass = []

    # deletes classes from database
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
    # creates the title of the window
    title = Label(frame, text="Assignments", font=("Arial", 20))
    title.pack() # places title on the top of teh window

    # gets all assignments under a certain teacher
    assignments = SQLfunctions.getAssignInfo(id)

    if assignments: # if assignments is not empty
        # creates the columns for the table
        columns = ("Assignment ID", "Title", "Due Date", "Class Name")
        # creates the table using the Treeview widget
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("Assignment ID", text="Assignment ID")
        tree.heading("Title", text="Title")
        tree.heading("Due Date", text="Due Date")
        tree.heading("Class Name", text="Class Name")

        tree.column("Assignment ID", width=50)
        tree.column("Title", width=150)
        tree.column("Due Date", width=60)
        tree.column("Class Name", width=150)

        # inserts assignment info
        for assignment in assignments:
            tree.insert("", "end", values=assignment)

        # places tre underneath of the title
        tree.pack(fill=BOTH, expand=True)

        # function to sort the table by a certain column
        def sort_by_column(tree, col, reverse):
            l = [(tree.set(k, col), k) for k in tree.get_children('')]
            l.sort(reverse=reverse)

            for index, (val, k) in enumerate(l):
                tree.move(k, '', index)

            tree.heading(col, command=lambda: sort_by_column(tree, col, not reverse))

        # sort by id
        sort_by_id_button = Button(frame, text="Sort by Assignment ID",
                                   command=lambda: sort_by_column(tree, "Assignment ID", False))
        sort_by_id_button.pack(side=LEFT, padx=10, pady=10)

        # sort by title
        sort_by_title_button = Button(frame, text="Sort by Title", command=lambda: sort_by_column(tree, "Title", False))
        sort_by_title_button.pack(side=LEFT, padx=10, pady=10)
    else: # if assignments is empty
        no_data_label = Label(frame, text="No assignments found.", font=("Arial", 16))
        no_data_label.pack()

def submissionObjects(frame, id):
    title = Label(frame, text="Submissions", font=("Arial", 20)) # creates the title of the window
    title.pack() # places title on the top of teh window

    # gets all submissions under a certain teacher
    submissions = SQLfunctions.getSubmissions(id)

    # if submissions is not empty create tree view of submissions
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
    else: # if submissions is empty
        no_data_label = Label(frame, text="No submissions found.", font=("Arial", 16))
        no_data_label.pack()

def submissionViewCreate(id):
    win = Tk() # creates window instance

    # sets the window size and position
    wWidth = 600
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    # window title
    win.title("Assignments")

    # creates a notebook from tkinter (allows for multiple tabs in one window)
    notebook = ttk.Notebook(win)
    notebook.grid()

    # sets frames for the different tabs
    assignments = Frame(notebook)
    submissions = Frame(notebook)

    # gets the assignment tab and submission tab information
    assignmentObjects(assignments, id)
    submissionObjects(submissions, id)

    # adds the frames to the notebook
    assignments.grid()
    submissions.grid()

    # adds the tabs to the window
    notebook.add(assignments, text="View Assignments")
    notebook.add(submissions, text="View Submissions")

    win.resizable(False, False)
    win.mainloop()

def createAssign(tID):
    win = Toplevel() # window instance
    win.title("Create Assignment") # window title

    # sets the window size and position
    wWidth = 500
    wHeight = 350
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleL = Label(win, text="Create Assignment", font=("Arial", 20))
    titleL.place(relx=0.25, rely=0.05, relheight=0.13, relwidth=0.5)

    assignName = Label(win, text="Assignment Title:", font=("Arial", 16))
    assignName.place(relx=0.03, rely=0.25, relheight=0.13, relwidth=0.4)

    nameVar = tkinter.StringVar()
    nameEntry = Entry(win, textvariable=nameVar, font=('Arial', 12), width=27)
    nameEntry.place(relx=0.4, rely=0.28, relheight=0.07, relwidth=0.5)

    classLabel = Label(win, text="Class:", font=("Arial", 16))
    classLabel.place(relx=0.225, rely=0.4, relheight=0.13, relwidth=0.2)

    # gets all classes under a certain teacher
    class_list = SQLfunctions.getClass(tID)

    classes = class_list
    clicked = StringVar()
    clicked.set("Class")
    classMenu = OptionMenu(win, clicked, *classes)
    classMenu.place(relx=0.4, rely=0.41, relheight=0.1, relwidth=0.25)

    # creates a variable to store the date
    dateVar = StringVar()

    # creates a calendar window
    def calendar():
        top = Toplevel(win)
        top.title("Choose Date")

        today = datetime.date.today()
        cal = Calendar(top, selectmode='day', year=today.year, month=today.month, day=today.day)
        cal.pack(pady=20)

        # returns the selected date
        def get_date():
            date = cal.selection_get()
            dateVar.set(date)
            top.destroy()

        select = Button(top, text="Select", font=("Arial", 14), command=get_date)
        select.pack()


    dueLabel = Label(win, text="Due:", font=("Arial", 16))
    dueLabel.place(relx=0.26, rely=0.55, relheight=0.1, relwidth=0.15)

    dateEntry = Entry(win, textvariable=dateVar, font=('Arial', 12), width=15, state='readonly')
    dateEntry.place(relx=0.7, rely=0.55, relheight=0.1, relwidth=0.25)

    dueButton = Button(win, text="Choose Date", font=("Arial", 10), command=lambda: calendar())
    dueButton.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.25)

    nextButton = Button(win, text="Next", font=("Arial", 16),
                        command=lambda: SQLfunctions.createAssign(tID, win, nameVar.get(), clicked.get(),
                                                                  dateVar.get()))
    nextButton.place(relx=0.6, rely=0.7, relheight=0.13, relwidth=0.2)

    cancelButton = Button(win, text="Cancel", font=("Arial", 16), command=lambda: win.destroy())
    cancelButton.place(relx=0.2, rely=0.7, relheight=0.13, relwidth=0.2)

    nameEntry.focus()
    win.resizable(False, False)
    win.mainloop()

def nextAssign(assign_id, win):
    win.destroy()
    createQs(assign_id)

def createQs(assign_id):
    win = Toplevel() # window instance
    win.title("Create Question") # window title

    # sets the window size and position
    wWidth = 650
    wHeight = 500
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    titleLabel = Label(win, text="Add Question", font=("Arial", 20))
    titleLabel.place(relx=0.25, rely=0.01, relheight=0.13, relwidth=0.5)

    questionLabel = Label(win, text="Question:", font=("Arial", 16))
    questionLabel.place(relx=0.05, rely=0.12, relheight=0.05, relwidth=0.15)

    quest = StringVar()
    questionEntry = Entry(win, textvariable=quest, font=('Arial', 12))
    questionEntry.place(relx=0.23, rely=0.12, relheight=0.06, relwidth=0.7)

    marksLabel = Label(win, text="Marks:", font=("Arial", 16))
    marksLabel.place(relx=0.06, rely=0.22, relheight=0.05, relwidth=0.15)

    marksEntry = Text(win, font=("Arial", 16))
    marksEntry.place(relx=0.23, rely=0.22, relheight=0.06, relwidth=0.1)

    answerLabel = Label(win, text="Answer:", font=("Arial", 16))
    answerLabel.place(relx=0.05, rely=0.32, relheight=0.05, relwidth=0.15)

    answerEntry = Text(win, font=('Arial', 10))
    answerEntry.place(relx=0.23, rely=0.32, relheight=0.5, relwidth=0.7)

    typeLabel = Label(win, text="Type:", font=("Arial", 16))
    typeLabel.place(relx=0.4, rely=0.22, relheight=0.06, relwidth=0.15)

    # type of question options
    options = ["Standard answer", "Calculation"]
    clicked = StringVar()
    clicked.set("Type of Question")
    typeMenu = OptionMenu(win, clicked, *options)
    typeMenu.place(relx=0.52, rely=0.21, relheight=0.08, relwidth=0.22)

    nextButton = Button(win, text="Add question", font=("Arial", 16), command=lambda: SQLfunctions.addQuestion(assign_id, quest.get(), answerEntry.get("1.0", "end"), marksEntry.get("1.0", "end"), clicked.get(), win))
    nextButton.place(relx=0.55, rely=0.85, relheight=0.1, relwidth=0.22)

    cancelButton = Button(win, text="Finish", font=("Arial", 16), command=lambda: win.destroy())
    cancelButton.place(relx=0.23, rely=0.85, relheight=0.1, relwidth=0.2)

    questionEntry.focus()
    win.resizable(False, False)
    win.mainloop()

def studentProgress(s_id):
    win = Toplevel()
    win.title("Progress")

    wWidth = 600
    wHeight = 400
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    submissions = SQLfunctions.getStudentProgress(s_id)

    if submissions:
        columns = ("Title", "Submission ID", "Mark", "Submission Date")
        tree = ttk.Treeview(win, columns=columns, show="headings")
        tree.heading("Title", text="Assignment Title")
        tree.heading("Submission ID", text="Submission ID")
        tree.heading("Mark", text="Mark")
        tree.heading("Submission Date", text="Submission Date")

        tree.column("Title", width=150)
        tree.column("Submission ID", width=100)
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

        sort_by_id_button = Button(win, text="Sort by Submission ID", command=lambda: sort_by_column(tree, "Submission ID", False))
        sort_by_id_button.pack(side=LEFT, padx=10, pady=10)

        sort_by_title_button = Button(win, text="Sort by Title", command=lambda: sort_by_column(tree, "Title", False))
        sort_by_title_button.pack(side=LEFT, padx=10, pady=10)
    else:
        no_data_label = Label(win, text="No submissions found.", font=("Arial", 16))
        no_data_label.pack()

    win.resizable(False, False)
    win.mainloop()


def checkVal(email, password, window, name, teacherID):
    if validEmail(email) == False: # validates entered email
        mg.showwarning("Invalid email", "The email you have entered is invalid")
    elif SQLfunctions.checkEmail(email) == False: # checks if email is already in use
        mg.showwarning("Email taken", "This email is already taken")
    #elif verifyEmail(email) == False: # verifies that entered email is real
        #mg.showwarning("Invalid email", "The email you have entered is invalid")
    elif validatePassword(password) == False: # validates password entered
        mg.showwarning("Invalid password", "Your password must include: an uppercase letter, a "
                                                   "lowercase letter, a number, a special character (!@_&) and "
                                                   "between 8 and 20 characters")
    else:
        # If all checks pass, create the account and send student confirmation email
        SQLfunctions.registerAcc(email, password, name, teacherID)
        sendEmailCreate(email, password, name)
        mg.showinfo("Account Created", "Account has been created and details have been sent to student")
        window.destroy()

def getVal(nameBox, emailBox, passBox, repassBox, window, teacherID):
    # Strip gets rid of whitespace at the beginning or the end of the string
    # 1.0 and end-1c is where the indexing starts and ends
    name = nameBox.get("1.0", "end-1c")
    email = emailBox.get("1.0", "end-1c").strip().lower()
    password = passBox.get().strip()
    repassword = repassBox.get().strip()

    if len(name) < 1 or len(email) < 1 or len(password) < 1 or len(repassword) < 1:
        mg.showwarning("Empty Field", "Please fill out all fields")
    else:
        # Capitalises the first letter of the first name and surname for the database
        space = 0
        for i in range(len(name)):
            if name[i].isspace():
                space = i
        if len(name) < 5:
            mg.showwarning("Name too short", "Please enter your full name")
        else:
            # Capitalises the first letter of the first name and surname
            name = name[0].capitalize() + name[1:space] + " " + name[space + 1].capitalize() + name[space + 2:]

        if password != repassword:
            mg.showwarning("Passwords don't match", "Passwords don't match. Please try again")
        else:
            checkVal(email, password, window, name, teacherID)

def togglePass(passBox):
    if passBox.cget("show") == "•":
        passBox.config(show="")
    else:
        passBox.config(show="•")


def createBox(teacherID):
    window = Toplevel() # Creates a new window

    # calculates middle of the screen
    wWidth = 500
    wHeight = 350
    xCord = int((window.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((window.winfo_screenheight() / 2) - (wHeight / 2))
    window.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")
    window.resizable(False, False)

    window.title("Register Account")

    # Variables for the text boxes
    password_var = tkinter.StringVar()
    repassword_var = tkinter.StringVar()

    # Title label
    titleLabel = Label(window, text="Register Account")
    titleLabel.config(font=("Arial", 20))
    titleLabel.place(relx=0.27, rely=0.01, relheight=0.11, relwidth=0.5)

    # Register button
    registerButton = Button(window, text="Register Account", command=lambda: getVal(nameBox, emailBox, passBox,
                                                                                    repassBox, window, teacherID))
    registerButton.config(font=("Arial", 16))
    registerButton.place(relx=0.12, rely=0.7, relheight=0.11, relwidth=0.4)

    # Exit button
    exitButton = Button(window, text="Exit", command=lambda: window.destroy())
    exitButton.config(font=("Arial", 16))
    exitButton.place(relx=0.65, rely=0.7, relheight=0.11, relwidth=0.15)

    # Name label and text box
    nameLabel = Label(window, text="Full Name:")
    nameLabel.config(font=("Arial", 14))
    nameLabel.place(relx=0.05, rely=0.125, relheight=0.11, relwidth=0.4)
    nameBox = Text(window, height=1, width=30)
    nameBox.place(relx=0.37, rely=0.16, relheight=0.06, relwidth=0.48)

    # Email label and text box
    emailLabel = Label(window, text="Email Address:")
    emailLabel.config(font=("Arial", 14))
    emailLabel.place(relx=0.06, rely=0.255, relheight=0.1, relwidth=0.3)
    emailBox = Text(window, height=1, width=30)
    emailBox.place(relx=0.37, rely=0.28, relheight=0.06, relwidth=0.48)

    # Password label and text box
    passLabel = Label(window, text="Password:")
    passLabel.config(font=("Arial", 14))
    passLabel.place(relx=0.15, rely=0.38, relheight=0.1, relwidth=0.2)
    # Makes whatever is entered into bullet points
    passBox = Entry(window, textvariable=password_var, font=('Arial', 12), show='•', width=27)
    passBox.place(relx=0.37, rely=0.4, relheight=0.06, relwidth=0.48)

    # Re-type label and text box
    repassLabel = Label(window, text="Re-type Password:")
    repassLabel.config(font=("Arial", 14))
    repassLabel.place(relx=0.022, rely=0.5, relheight=0.1, relwidth=0.32)
    repassBox = Entry(window, textvariable=repassword_var, font=('Arial', 12), show='•', width=27)
    repassBox.place(relx=0.37, rely=0.52, relheight=0.06, relwidth=0.48)


    # Show password buttons
    showPassImg = PhotoImage(file="./Pictures/showPassword.png")
    showPassImg = showPassImg.subsample(15, 15)
    showPass = Button(window, image=showPassImg, borderwidth=0, command=lambda: togglePass(passBox))
    showPass.place(relx=0.87, rely=0.39, relheight=0.07, relwidth=0.1)

    showRePass = Button(window, image=showPassImg, borderwidth=0, command=lambda: togglePass(repassBox))
    showRePass.place(relx=0.87, rely=0.51, relheight=0.07, relwidth=0.1)

    nameBox.focus()
    window.mainloop()


if __name__ == "__main__":
    # changeEmailUI("test", "test")
    # changePassUI("test", "test", "Admin")
    # createClassUI(1)
    # stuListUI(1)
    # createAssignmentNumber()
    # sendEmailOTP("kostispapd@outlook.com", "123456")
    # deleteClassUI(1)
    # submissionViewCreate(1)
    # createQs(1)
    createAssign(1)
    # studentProgress(3)
    pass
