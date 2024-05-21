import psycopg2
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
connector_key = os.getenv("DB_KEY")

try:
    conn = psycopg2.connect(connector_key)
    print("Connected to the database")
except Exception as e:
    print("Connection failed")
    print("Error: ", e)


#with psycopg2.connect(connector_key) as conn:
#    with conn.cursor() as cursor:
#        cursor.execute("SELECT * FROM AdminAcc")
#        cursor.fetchone()
#        for record in cursor:
#            print(record)
