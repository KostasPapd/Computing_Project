import psycopg2
import os
from dotenv import load_dotenv
from tkinter import messagebox as mg
import processWindows

# Takes the password, adds the salt, hashes it and returns the hashed password
def hashPassword(password):
    import hashlib
    salt = "lr4h"
    password = password + salt
    hash_object = hashlib.sha256(password.encode())
    hashPass = hash_object.hexdigest()
    return hashPass

# Searches the database and gets the teacher ID and returns it
def getTeachID(tName):
    load_dotenv() # loads the .env file
    connector_key = os.getenv("DB_KEY") # takes the database key from the .env file
    try:
        conn = psycopg2.connect(connector_key) # connects to the database
        cur = conn.cursor() # creates a cursor
        cur.execute(f"SELECT id FROM admin_acc WHERE name = %s", (tName,))
        res = cur.fetchone()
        if res:
            return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to find ID")
        return None

# Takes in all the parameters and adds them to the main_acc database as a new account
def registerAcc(email, password, name, teacher):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(password)
        email = email.lower()
        cur.execute(f"INSERT INTO main_acc (name, password, email, teacher_id) "
                    f"VALUES (%s, %s, %s, %s)", (name, passw, email, teacher))
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create account")

# checks if the email entered is already in use
def checkEmail(email):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        email = email.lower()
        cur.execute(f"SELECT email FROM main_acc WHERE email = %s", (email,))
        res = cur.fetchone()
        if res is not None:
            return False
        else:
            return True
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check if user exists. {e}")

# checks the log in info and checks if the user has admin rights
def checkLogIn(user, passw):
    # loads the .env file
    load_dotenv()
    # takes the database key from the .env file
    connector_key = os.getenv("DB_KEY")
    try:
        # connects to the database
        conn = psycopg2.connect(connector_key)
        # creates a cursor
        cur = conn.cursor()
        # hashes the password entered
        passw = hashPassword(passw)
        # checks if the user is a student
        cur.execute(f"SELECT * FROM main_acc WHERE email = %s AND password = %s", (user, passw))
        res = cur.fetchone()
        # if the user is a student, return the user's information (Student, name, email and password)
        if res is not None:
            return "Student", res[1], user, passw
        # if the user is not a student, check if the user is an admin
        else:
            try:
                cur.execute(f"SELECT * FROM admin_acc WHERE email = %s AND password = %s", (user, passw))
                result = cur.fetchone()
                if result is not None:
                    # if the user is an admin, return the user's information (Admin, name, teacherId, password and email)
                    return "Admin", result[3], getTeachID(result[3]), passw, user
                else:
                    # returns None if the user doesn't exist
                    return None
            except Exception as e:
                # error handling
                mg.showwarning("Connection Failed", f"Unable to check if user exists.{e}")
    except Exception as e:
        # error handling
        mg.showwarning("Connection Failed", f"Unable to check if user exists. {e}")


# changes the password of the user
def changePass(user, level, passw):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(passw)
        if level == "Admin":
            cur.execute(f"UPDATE admin_acc SET password = %s WHERE email = %s", (passw, user))
        else:
            cur.execute(f"UPDATE main_acc SET password = %s WHERE email = %s", (passw, user))
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to change password.")


# changes the email of the user
def changeEmail(level, user, email):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        if level == "Admin":
            cur.execute("UPDATE admin_acc SET email = %s WHERE name = %s", (email, user))
        else:
            cur.execute("UPDATE main_acc SET email = %s WHERE email = %s", (email, user))
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to change email. {e}")

# gets a list off all students under a teacher's name (used to create classes)
def getStudents(teacher):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM main_acc WHERE teacher_id = %s", (teacher,))
        res = cur.fetchall()
        if res is not None:
            names = [row[0] for row in res]  # Extract the names from the tuples
            return names
        else:
            return []
    except Exception as e:
        print(e)
        mg.showwarning("Connection Failed", "Unable to fetch students.")
        return []


# creates a class in the database
def createClass(name, teacher, stuList):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        table_name = f"\"{name}_{teacher}\""  # Creates the table name
        cur.execute(f"CREATE TABLE %s (student_id INT PRIMARY KEY , student_name varchar(255))", (table_name,))  # Creates the table
        cur.execute(f"INSERT INTO stud_classes (class_names, teacher_id) VALUES (%s, %s)", (name, teacher))  # Inserts the class into the table
        for student in stuList:
            cur.execute("SELECT id FROM main_acc WHERE name = %s", (student,))
            student_id = cur.fetchone()[0]

            # Inserts the students into the table
            cur.execute(f"INSERT INTO {table_name} (student_id, student_name) VALUES (%s, %s)", (student_id, student))

        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create class.")

# gets all of the classes under a teacher's name
def getClass(t_ID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT class_names FROM stud_classes WHERE teacher_id = %s", (t_ID,))
        res = cur.fetchall()
        if res is not None:
            names = [row[0] for row in res]  # Extract the names from the tuples
            return names
        else:
            return []
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to search for classes.")
        return []

# gets the id of a class
def getClassID(className):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT id FROM stud_classes WHERE class_names = %s", (className,))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", e)

# creates a new table and adds the assignment to the assignments table
def createAssign(t_ID, win, title, className, dueDate):
    if len(title) == 0 or len(className) == 0 or len(dueDate) == 0:
        mg.showwarning("Empty Fields", "Please fill in all fields.")
    else:
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            table_name = f"\"a{processWindows.createAssignmentNumber()}\""
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()

            class_id = getClassID(className)
            if class_id is None:
                mg.showerror("Class Not Found", "Class not found.")
            else:
                class_id = f"{class_id}"

            cur.execute(f"INSERT INTO assignments (title_id, title, class_id, due_date, teacher_id) VALUES "
                        f"(%s, %s, %s, %s, %s)", (table_name, title, class_id, dueDate, t_ID))

            cur.execute(f"CREATE TABLE {table_name} (questionNum SERIAL PRIMARY KEY, "
                        f"assignment_id INT REFERENCES assignments(assign_id),"
                        f"question varchar(255), answer varchar(255), marks int, question_type varchar(255))")
            conn.commit()

            assign_id = getAssignID(table_name)
            processWindows.nextAssign(assign_id, win)

        except Exception as e:
            mg.showwarning("Connection Failed", f"Unable to create assignment. {e}")
            print(e)

def getAssignName(assignID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT title_id FROM assignments WHERE assign_id = %s", (assignID,))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get assignment name. {e}")
        return None

def addQuestion(assign_id, question, answer, marks, question_type, win):
    if len(question) == 0 or len(answer) == 0 or len(marks) == 0 or len(question_type) == 0:
        mg.showwarning("Empty Fields", "Please fill in all fields.")
    else:
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()
            table_name = getAssignName(assign_id)
            cur.execute(f"INSERT INTO {table_name} (assignment_id, question, answer, marks, question_type) VALUES (%s, %s, %s, %s, %s)",
                        (assign_id, question, answer, marks, question_type))
            conn.commit()
            processWindows.nextAssign(assign_id, win)
        except Exception as e:
            mg.showwarning("Connection Failed", f"Unable to add question. {e}")

# gets the specified question
def getQuest(num, assignName):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT question FROM {assignName} WHERE questionnum = %s", (str(num),))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get questions. {e}")

# checks what type of question a question is (calculation or standard answer)
def checkType(assign_name, question_num):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT question_type FROM {assign_name} WHERE questionnum = %s", str(question_num))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check question type. {e}")
        return None

# gets the assignment id
def checkAssignmentNumber(ID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM assignments WHERE title_id = %s", (ID,))
        res = cur.fetchone()
        return res is not None
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check title ID. {e}")
        return False
    finally:
        if conn:
            conn.close()

# gets the student and teacher id
def getIDs(name):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT id, teacher_id FROM main_acc WHERE name = %s", (name,))
        res = cur.fetchone()
        if res:
            return res[0], res[1]
        else:
            return None
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get ID. {e}")
        return None
    finally:
        if conn:
            conn.close()

# gets the last question from an assignment
def getLast(assign_name):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT questionnum FROM {assign_name} WHERE questionnum = (SELECT MAX(questionnum) FROM {assign_name})")
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get last question. {e}")
        return None
    finally:
        if conn:
            conn.close()

# gets the answer for the specified question
def getAnsw(assignName, questionNum):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT answer, marks FROM {assignName} WHERE questionnum = %s", (str(questionNum)))
        res = cur.fetchone()
        return res
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get answer. {e}")
        return None

# gets the assignment id
def getAssignID(assignName):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT assign_id FROM assignments WHERE title_id = %s", (assignName,))
        res = cur.fetchone()
        if res:
            return res[0]
        else:
            mg.showwarning("No Results", "No assignment found with the given name.")
            return None
    except Exception as e:
        print(e)
        mg.showwarning("Connection Failed", f"Unable to get assignment ID. {e}")
        return None

# saves the student's submission
def saveSub(assignID, studentID, date, mark):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("INSERT INTO submissions (assignment_id, student_id, submission_date, mark) VALUES (%s, %s, %s, %s)",
                    (assignID, studentID, date, mark))
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to save submission. {e}")

# deletes the specified class
def deleteClass(t_id, classes):
    for i in classes:
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()
            table_name = f"\"{i}_{t_id}\""
            cur.execute(f"DROP TABLE {table_name}")
            cur.execute(f"DELETE FROM stud_classes WHERE class_names = %s", (i,))
            conn.commit()
            return True
        except Exception as e:
            mg.showwarning("Connection Failed", f"Unable to delete class. {e}")
            return False

# gets all the submissions for a teacher
def getSubmissions(t_id):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("""
                    SELECT a.title, s.subm_id, m.name, s.mark, s.submission_date
                    FROM submissions s
                    JOIN assignments a ON s.assignment_id = a.assign_id
                    JOIN main_acc m ON s.student_id = m.id
                    WHERE a.teacher_id = %s
                """, (t_id,))
        res = cur.fetchall()
        if res:
            return res
        else:
            return None
    except Exception as e:
         mg.showwarning("Connection Failed", f"Unable to get submissions. {e}")

# gets all the assignments for a teacher
def getAssignInfo(t_id):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("""
                    SELECT a.assign_id, a.title, a.due_date, sc.class_names
                    FROM assignments a
                    JOIN stud_classes sc ON a.class_id = sc.id
                    WHERE a.teacher_id = %s
                """, (t_id,))
        res = cur.fetchall()
        if res:
            return res
        else:
            return None
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get assignments. {e}")

# gets the student's name
def getName(sId):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT name FROM main_acc WHERE id = %s", (sId,))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get name. {e}")
        return None

# gets the student's id
def getID(email):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT id FROM main_acc WHERE email = %s", (email,))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get ID. {e}")
        return None

# gets the student's progress
def getStudentProgress(s_id):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("""
                    SELECT a.title, s.subm_id, s.mark, s.submission_date
                    FROM submissions s
                    JOIN assignments a ON s.assignment_id = a.assign_id
                    WHERE s.student_id = %s
                """, (s_id,))
        res = cur.fetchall()
        if res:
            return res
        else:
            return None
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get progress. {e}")

if __name__ == "__main__":
    # For testing
    # getTeachID("Kostas Papadopoulos")
    # getStudents("Kostas Papadopoulos")
    # registerAcc("test", "test", "test", 1)
    # checkType("test_assignment", 1)
    # print(getQuest(1, "a00000001"))
    # print(getClass(1))
    # print(getSubmissions(1))
    # print(getAssignInfo(1))
    print(hashPassword("Password1!"))
    pass
