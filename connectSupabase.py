import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
connector_key = os.getenv("DB_KEY")

try:
    conn = psycopg2.connect(connector_key)
    print("Connected to the database")
    cur = conn.cursor()
    cur.execute("INSERT INTO admin_acc (username, password) VALUES ('ADMTest', 'ADMTestPass')")
    conn.commit()
    cur.execute("SELECT * FROM admin_acc")
    for table in cur.fetchall():
        print(table)
except Exception as e:
    print("Connection failed")
    print("Error: ", e)

