"""
All the SQL/database functions will go in this program

CHANGE THE CODE SO NO INJECTIONS
e.g.
sql = "SELECT id FROM admin_acc WHERE name = %s"
cur.execute(sql, (tName))

Add to here:
Inserts new class into stud_classes table
"""

import psycopg2
import os
from dotenv import load_dotenv
from tkinter import messagebox as mg
import processWindows
import assignProcess

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
        cur.execute(f"SELECT id FROM admin_acc WHERE name = '{tName}'")
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
        cur.execute(f"INSERT INTO main_acc (name, password, email, teacher_id) "
                    f"VALUES ('{name}', '{passw}', '{email}', '{teacher}')")
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
        cur.execute(f"SELECT email FROM main_acc WHERE email = '{email}'")
        res = cur.fetchone()
        if res is not None:
            return False
        else:
            return True
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check if user exists. {e}")

# checks the log in info and checks if the user has admin rights
def checkLogIn(user, passw):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(passw)
        cur.execute(f"SELECT * FROM main_acc WHERE email = '{user}' AND password = '{passw}'")
        res = cur.fetchone()
        if res is not None:
            return "Student", res[1], user, passw
        else:
            try:
                cur.execute(f"SELECT * FROM admin_acc WHERE email = '{user}' AND password = '{passw}'")
                result = cur.fetchone()
                if result is not None:
                    return "Admin", result[3], getTeachID(result[3]), passw, user
                else:
                    return None
            except Exception as e:
                mg.showwarning("Connection Failed", "Unable to check if user exists.")
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check if user exists. {e}")


# changes the password of the user
def changePass(user, level, passw):
    if level == "Admin":
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()
            passw = hashPassword(passw)
            cur.execute(f"UPDATE admin_acc SET password = '{passw}' WHERE email = '{user}'")
            conn.commit()
        except Exception as e:
            mg.showwarning("Connection Failed", "Unable to change password.")
    else:
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()
            passw = hashPassword(passw)
            cur.execute(f"UPDATE main_acc SET password = '{passw}' WHERE email = '{user}'")
            conn.commit()
        except Exception as e:
            mg.showwarning("Connection Failed", "Unable to change password.")

# changes the email of the user
def changeEmail(level, user, email):
    if level == "Admin":
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()
            cur.execute(f"UPDATE admin_acc SET email = '{email}' WHERE email = '{user}'")
            conn.commit()
        except Exception as e:
            mg.showwarning("Connection Failed", "Unable to change email.")
    else:
        load_dotenv()
        connector_key = os.getenv("DB_KEY")
        try:
            conn = psycopg2.connect(connector_key)
            cur = conn.cursor()
            cur.execute(f"UPDATE main_acc SET email = '{email}' WHERE email = '{user}'")
            conn.commit()
        except Exception as e:
            mg.showwarning("Connection Failed", "Unable to change email.")

# gets a list off all students under a teacher's name (used to create classes)
def getStudents(teacher):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM main_acc WHERE teacher_id = '{teacher}'")
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


#CHANGE SO IT JUST CHANGES THE CLASS ID ON THE main_acc TABLE
# creates a class in the database
def createClass(name, teacher, stuList):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        table_name = f"\"{name}_{teacher}\""  # Creates the table name
        cur.execute(f"CREATE TABLE {table_name} (student_id INT PRIMARY KEY , student_name varchar(255))")  # Creates the table
        cur.execute(f"INSERT INTO stud_classes (class_names, teacher_id) VALUES ('{name}', '{teacher}')")  # Inserts the class into the table
        for student in stuList:
            cur.execute("SELECT id FROM main_acc WHERE name = %s", (student,))
            student_id = cur.fetchone()[0]

            # Inserts the students into the table
            cur.execute(f"INSERT INTO {table_name} (student_id, student_name) VALUES (%s, %s)", (student_id, student))

        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create class.")

# gets all the students in a specified class
def getClass(t_ID):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT class_names FROM stud_classes WHERE teacher_id = '{t_ID}'")
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
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        table_name = f"\"a{processWindows.createAssignmentNumber()}\""
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()

        class_id = getClassID(className)
        if class_id is None:
            class_id = 'NULL'
        else:
            class_id = f"'{class_id}'"

        cur.execute(f"INSERT INTO assignments (title_id, title, class_id, due_date, teacher_id) VALUES "
                    f"('{table_name}', '{title}', {class_id}, '{dueDate}', '{t_ID}')")

        cur.execute(f"CREATE TABLE {table_name} (questionNum SERIAL PRIMARY KEY, "
                    f"assignment_id INT REFERENCES assignments(assign_id),"
                    f"question varchar(255), answer varchar(255), marks int, question_type varchar(255))")
        conn.commit()
        assignProcess.nextAssign(t_ID, win)
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to create assignment. {e}")


def addQuestion():
    pass

# gets the specified question
def getQuest(num, assignName):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT question FROM {assignName} WHERE questionnum = %s", (num,))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get questions. {e}")

# checks what type of question (calculation or written) a question is
def checkType(assign_name, question_num):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT question_type FROM {assign_name} WHERE questionnum = {question_num}")
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

def getAnsw(assignName, questionNum):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT answer, marks FROM {assignName} WHERE questionnum = {questionNum}")
        res = cur.fetchone()
        return res
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to get answer. {e}")
        return None

def getAssignID(assignName):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        assignName = f"\"{assignName}\""
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute("SELECT assign_id FROM assignments WHERE title_id = %s", (assignName,))
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        print(e)
        mg.showwarning("Connection Failed", f"Unable to get assignment ID. {e}")
        return None

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
        print(e)
        mg.showwarning("Connection Failed", f"Unable to save submission. {e}")

if __name__ == "__main__":
    # For testing
    # getTeachID("Kostas Papadopoulos")
    # getStudents("Kostas Papadopoulos")
    # registerAcc("test", "test", "test", 1)
    # checkType("test_assignment", 1)
    # print(getQuest(1, "a00000001"))
    print(getClass(1))
    pass
