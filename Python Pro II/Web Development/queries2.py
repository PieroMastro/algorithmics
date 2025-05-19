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

def add_question():
    questions = [
        ('¿Cuántos meses en un año tienen 28 días?', 'Todos', 'Uno', 'Ninguno','Dos'),
        ('¿Qué aspecto tendrá el acantilado verde si se cae en el Mar Rojo?', 'Mojado', 'Rojo', 'No cambiará', 'Púrpura'),
        ('¿Con qué mano es mejor mezclar el té?', 'Con una cuchara', 'Derecha', 'Izquierda', 'Cualquiera'),
        ('¿Qué no tiene longitud, profundidad, ancho, o altura pero puede medirse?', 'Tiempo', 'Estupidez', 'El mar','Aire'),
        ('¿Cuándo es posible sacar agua con una red?', 'Cuando el agua está congelada', 'Cuando no hay peces', 'Cuando los peces de colores nadan lejos', 'Cuando la red se rompe'),
        ('¿Qué es más grande que un elefante y no pesa nada?', 'La sombra de un elefante','Un globo','Un paracaídas', 'Una nube')
    ]

    start()
    cursor.executemany('''INSERT INTO question (name, answer, incorrect_option_1, incorrect_option_2, incorrect_option_3)
            VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()

def add_quiz():
    quizzes = [
        ('Own game',),
        ('¿Quién quiere ser millonario?',),
        ('El más inteligente',)
    ]
    start()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizzes)
    conn.commit()
    close()

def add_links():
    start()
    query = '''
        INSERT INTO quiz_content (quiz_id, question_id)
        VALUES (?, ?)
    '''
    link = input('Desea agregar una pregunta a un cuestionario? (y/n)')
    while link.lower() == 'y':
        try:
            quiz_id = int(input('Ingrese el id del cuestionario: '))
            question_id = int(input('Ingrese el id de la pregunta: '))
            cursor.execute(query, [quiz_id, question_id])
            conn.commit()
        except ValueError:
            print('Ingrese un número válido')
        finally:
            link = input('Desea agregar una pregunta a un cuestionario? (y/n)')
    close()

def get_question_after(question_id=0, quiz_id=1):
    start()
    query = '''
        SELECT quiz_content.id, question.name, question.answer, question.wrong_option_1, wrong_option_2, wrong option 3
        FROM quiz_content, question
        WHERE quiz_content.question_id = question.id
        AND quiz_content.id > (?) AND quiz_content.quest_id == (?)
        ORDER BY quiz_content.id
        LIMIT 1
        '''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result

def show(table):
    start()
    query = f'SELECT * FROM {table}'
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('quiz')
    show('question')
    show('quiz_content')

def main():
    clear_db()
    create_tables()
    add_question()
    add_quiz()
    add_links()
    show_tables()

if __name__ == '__main__':
    main()
