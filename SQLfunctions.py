# all the sql will go in this module

def hashPassword(password):
    import hashlib
    salt = "lr4h"
    password = password + salt
    hash_object = hashlib.sha256(password.encode())
    hashPass = hash_object.hexdigest()
    return hashPass


def registerAcc(username, email, password, name, school, level):
    import psycopg2
    import os
    from dotenv import load_dotenv
    from tkinter import messagebox as mg

    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        passw = hashPassword(password)
        cur.execute(f"INSERT INTO main_acc (level, name, username, password, email, school) "
                    f"VALUES ('{level}', '{name}', '{username}', '{passw}', '{email}', '{school}')")
        conn.commit()
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to create account")

def checkUser(user):
    import psycopg2
    import os
    from dotenv import load_dotenv
    from tkinter import messagebox as mg

    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        cur.execute(f"SELECT username FROM main_acc WHERE username = '{user}'")
        res = cur.fetchone()
        if res is not None:
            return False
        else:
            return True
    except Exception as e:
        mg.showwarning("Connection Failed", "Unable to check if user exists")
