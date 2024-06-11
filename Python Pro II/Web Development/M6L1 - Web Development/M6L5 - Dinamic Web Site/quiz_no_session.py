from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after

quiz = 0
last_question = 0

def index():
    global quiz, last_question
    max_quiz = 3
    quiz = randint(1, max_quiz)
    last_question = 0
    return '<a href= "/test">Cargando cuestionario</a>'

def test():
    global last_question
    result = get_question_after(last_question, quiz)
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        last_question = result[0]
        return f'<h1> {quiz} <br>{result} </h1'

def result():
    return 'Cuestionario completado!'

# Crear un objeto de aplicación web:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index) # crea una regla para la URL '/'
app.add_url_rule('/test', 'test', test) # crea una regla para la URL '/test'
app.add_url_rule('/result', 'result', result) # crea una regla para la URL '/test'

if __name__ == '__main__':
    # Iniciar el servidor web:
    app.run()
