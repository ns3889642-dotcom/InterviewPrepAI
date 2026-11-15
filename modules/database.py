import sqlite3
from datetime import datetime

DATABASE_PATH = "data/interview_history.db"


def create_table():
    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interview_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            score INTEGER NOT NULL,
            feedback TEXT,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_interview(subject, difficulty, question,
                   answer, score, feedback):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interview_history
        (subject, difficulty, question, answer,
         score, feedback, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        subject,
        difficulty,
        question,
        answer,
        score,
        feedback,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_interview_history():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT subject, difficulty, question,
               score, created_at
        FROM interview_history
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return records