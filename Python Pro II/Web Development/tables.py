import sqlite3

db_name = 'questions.db'
conn = None
cursor = None

def open(): 
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    conn.execute(query)
    conn.commit()

def create_tables():
    open()
    do('''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )'''
    )

    do(
        '''CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            incorrect_option_1 TEXT NOT NULL,
            incorrect_option_2 TEXT NOT NULL,
            incorrect_option_3 TEXT NOT NULL
        )'''
    )

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES question (id)
        )'''
    )
