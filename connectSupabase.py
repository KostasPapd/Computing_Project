import psycopg2
import os
from dotenv import load_dotenv
from SQLfunctions import hashPassword

load_dotenv()
connector_key = os.getenv("DB_KEY")

try:
    conn = psycopg2.connect(connector_key)
    print("Connected to the database")
    cur = conn.cursor()
    passw = hashPassword("Strakos12!")
    cur.execute(f"UPDATE admin_acc SET password = '{passw}' WHERE id = 1")
    conn.commit()
    cur.execute("SELECT * FROM admin_acc")
    for table in cur.fetchall():
        print(table)
except Exception as e:
    print("Connection failed")
    print("Error: ", e)

