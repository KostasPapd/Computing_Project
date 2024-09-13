"""
All the SQL/database functions will go in this program

CHANGE THE CODE SO NO INJECTIONS
e.g.
sql = "SELECT id FROM admin_acc WHERE name = %s"
cur.execute(sql, (tName))

Add to here:
Send email function - search for the email entered and then return all the student's information
"""

import psycopg2
import os
from dotenv import load_dotenv
from tkinter import messagebox as mg
import processWindows
import assignProcess


def hashPassword(password):
    import hashlib
    salt = "lr4h"
    password = password + salt
    hash_object = hashlib.sha256(password.encode())
    hashPass = hash_object.hexdigest()
    return hashPass

def getTeachID(tName):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT id FROM admin_acc WHERE name = '{tName}'")
        res = cur.fetchone()
        if res:
            return res[0]
        else:
            return None
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to find ID")
        return None

def registerAcc(email, password, name, teacher):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(password)
        cur.execute(f"INSERT INTO main_acc (class_id name, password, email, teacher_id) "
                    f"VALUES ('NULL', '{name}', '{passw}', '{email}', '{teacher}')")
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create account")
        print(e)


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
                    return "Admin", result[3], getTeachID(user), passw
                else:
                    return None
            except Exception as e:
                mg.showwarning("Connection Failed", "Unable to check if user exists.")
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check if user exists. {e}")



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
        mg.showwarning("Connection Failed", "Unable to fetch students.")
        return []

#CHANGE SO IT JUST CHANGES THE CLASS ID ON THE main_acc TABLE
def createClass(name, teacher, stuList):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        table_name = f"\"{name}_{teacher}\""  # Creates the table name
        cur.execute(f"CREATE TABLE {table_name} (student_name varchar(255))")  # Creates the table
        for student in stuList:
            # Inserts the students into the table
            cur.execute(f"INSERT INTO {table_name} (student_name) VALUES ('{student}')")
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create class.")

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

def createAssign(t_ID, win, title, className, dueDate):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        table_name = table_name = f"\"a{processWindows.createAssignmentNumber()}\""
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
        print(e)


def addQuestion():
    pass


def checkType(assign_name, question_num):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")
    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT question_type FROM {assign_name} WHERE question_id = {question_num}")
        res = cur.fetchone()
        return res[0]
    except Exception as e:
        mg.showwarning("Connection Failed", f"Unable to check question type. {e}")
        return None

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

if __name__ == "__main__":
    # For testing
    # getTeachID("Kostas Papadopoulos")
    # getStudents("Kostas Papadopoulos")
    # registerAcc("test", "test", "test", 1)
    # checkType("test_assignment", 1)
    pass
