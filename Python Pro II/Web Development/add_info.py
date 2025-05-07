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

    close()

def add_question():
    questions = [
        ('¿Cuántos meses en un año tienen 28 días?', 'Todos', 'Uno', 'Ninguno','Dos'),
        ('¿Qué aspecto tendrá el acantilado verde si se cae en el Mar Rojo?', 'Mojado', 'Rojo', 'No cambiará', 'Púrpura'),
        ('¿Con qué mano es mejor mezclar el té?', 'Con una cuchara', 'Derecha', 'Izquierda', 'Cualquiera'),
        ('¿Qué no tiene longitud, profundidad, ancho, o altura pero puede medirse?', 'Tiempo', 'Estupidez', 'El mar','Aire'),
        ('¿Cuándo es posible sacar agua con una red?', 'Cuando el agua está congelada', 'Cuando no hay peces', 'Cuando los peces de colores nadan lejos', 'Cuando la red se rompe'),
        ('¿Qué es más grande que un elefante y no pesa nada?', 'La sombra de un elefante','Un globo','Un paracaídas', 'Una nube')
    ]

    open()
    cursor.executemany('''INSERT INTO question (question, answer, incorrect_option_1, incorrect_option_2, incorrect_option_3)
            VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()

create_tables()
add_question()

open() # Abrir la conexión antes del SELECT
cursor.execute('SELECT * FROM question')
data = cursor.fetchall()
print(data)

def add_quiz():
    quizzes = [
        ('Own game'),
        ('¿Quién quiere ser millonario?'),
        ('El más inteligente')
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizzes)
    conn.commit()
    close()

def add_links():
    pass
