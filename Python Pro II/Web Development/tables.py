import sqlite3

db_name = 'quizzes.db'
conn = None
cursor = None

def start(): 
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

def close():
    cursor.close()
    conn.close()

def do(query):
    conn.execute(query)
    conn.commit()

def clear_db():
    start()
    cursor.execute('PRAGMA foreign_keys = OFF')
    do('DROP TABLE IF EXISTS quiz')
    do('DROP TABLE IF EXISTS question')
    do('DROP TABLE IF EXISTS quiz_content')
    close()

def create_tables():
    start()

    do('''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )''')

    do(
        '''CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            answer TEXT NOT NULL,
            incorrect_option_1 TEXT NOT NULL,
            incorrect_option_2 TEXT NOT NULL,
            incorrect_option_3 TEXT NOT NULL
        )''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES question (id)
        )''')

    close()
