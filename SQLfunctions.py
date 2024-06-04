# all the sql will go in this module
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

def registerAcc(email, password, name):
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(password)
        cur.execute(f"INSERT INTO main_acc (name, password, email) "
                    f"VALUES ('{name}', '{passw}', '{email}'")
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

def returnDetails(email):
    name = "name"
    password = "password"
    email = "email"
    return name, password, email
