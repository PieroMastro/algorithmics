def create()-> None:
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXIST quiz (id INTEGER PRIMARY KEY, name VARCHAR)''')

    do('''CREATE TABLE IF NOT EXIST question (
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR,) ''')

    do('''CREATE TABLE IF NOT EXIST quiz_content (
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        question_id INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES quiz (id),
        FOREIGN KEY (question_id) REFERENCES question (id)) ''')
    close()
    
    
def add_question():

    questions = [
        ('Hace cuanto salio el prisonero de Azkaban?', '2004', '2002', '1999', '2020'),
        ('Cuales mese tienen 28 dias?', 'todos', 'tres', 'ninguno', 'uno'),
        ('Cuando se estreno Hello Kitty?', '1974', '1956', '2000', '1980')
    ]

    open()

    cursor.executemany(''' INSERT INTO question (question, anwser, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)''', questions)
    conn.commit()
    close()

def add_quiz():

    quizes = [
        ('Pop Culture'),
        ('Python'),
        ('El mas inteligente')
    ]

    open()
    cursor.executemany(''' INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()

def link():

    cursor.executemany('''PRAGMA foreign_keys=on''')

    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)"

    anwser = input(' Desea agregar un vinculo (y/n)')

    while anwser != 'n':
        quiz_id = int(input('quiz id:' ))
        question_id = int(input('question id:' ))

        cursor.executemany(query, [quiz_id, question_id])
        conn.commit()
        anwser = input(' Desea agregar un vinculo (y/n)')

    close()


    
    