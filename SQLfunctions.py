"""
All the SQL/database functions will go in this program#

Add to here:
Send email function - search for the email entered and then return all the student's information
"""

import psycopg2
import os
from dotenv import load_dotenv
from tkinter import messagebox as mg


def hashPassword(password):
    import hashlib
    salt = "lr4h"
    password = password + salt
    hash_object = hashlib.sha256(password.encode())
    hashPass = hash_object.hexdigest()
    return hashPass

def registerAcc(email, password, name, teacher):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(password)
        cur.execute(f"INSERT INTO main_acc (name, password, email, teacher) "
                    f"VALUES ('{name}', '{passw}', '{email}', '{teacher}')")
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create account")


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
        mg.showwarning("Connection Failed", "Unable to check if user exists.")

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
                    return "Admin", result[3], user, passw
                else:
                    return None
            except Exception as e:
                mg.showwarning("Connection Failed", "Unable to check if user exists.")
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to check if user exists.")



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
        cur.execute(f"SELECT name FROM main_acc WHERE teacher = '{teacher}'")
        res = cur.fetchall()
        if res is not None:
            names = [row[0] for row in res]  # Extract the names from the tuples
            return names
        else:
            return []
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to fetch students.")
        return []


if __name__ == "__main__":
    # For testing
    getStudents("Kostas Papadopoulos")
    pass
