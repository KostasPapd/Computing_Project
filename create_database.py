import psycopg2
from dotenv import load_dotenv
import os


def create_tables():
    load_dotenv()
    connector_key = os.getenv("DB_KEY")

    commands = [
        """
        CREATE TABLE IF NOT EXISTS admin_acc(
            Id SERIAL PRIMARY KEY,
            Email VARCHAR(255) NOT NULL,
            Password VARCHAR(255) NOT NULL,
            Name VARCHAR(100) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS main_acc(
            Id SERIAL PRIMARY KEY,
            Name VARCHAR(100) NOT NULL,
            Password VARCHAR(255) NOT NULL,
            Email VARCHAR(255) NOT NULL,
            Teacher_id INT NOT NULL,
            FOREIGN KEY(Teacher_id) REFERENCES admin_acc(Id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS stud_classes(
            Id SERIAL PRIMARY KEY,
            Class_names VARCHAR(255) NOT NULL,
            Teacher_id INT NOT NULL,
            FOREIGN KEY(Teacher_id) REFERENCES admin_acc(Id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS assignments(
            Assign_id SERIAL PRIMARY KEY,
            Title VARCHAR(255) NOT NULL,
            Class_id INT NOT NULL,
            Due_date TIMESTAMP NOT NULL,
            Teacher_id INT NOT NULL,
            Title_id VARCHAR(9) NOT NULL,
            FOREIGN KEY(Class_id) REFERENCES stud_classes(Id),
            FOREIGN KEY(Teacher_id) REFERENCES admin_acc(Id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS submissions(
            Subm_id SERIAL PRIMARY KEY,
            Assignment_id INT NOT NULL,
            Student_id INT NOT NULL,
            Submission_date TIMESTAMP NOT NULL,
            Mark INT NOT NULL,
            FOREIGN KEY(Assignment_id) REFERENCES assignments(Assign_id),
            FOREIGN KEY(Student_id) REFERENCES main_acc(Id)
        )
        """
    ]

    try:
        conn = psycopg2.connect(connector_key)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_tables()