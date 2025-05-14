from flask import Flask, redirect, url_for, session
from db_scripts import get_question_after
from random import randint


quiz, last_question = 0, 0
app = Flask(__name__)

def index():
    global quiz, last_question
    max_quizzes = 3
    quiz = 1 #randint(1, max_quizzes)
    last_question = 0
    return '<a href=/test>Iniciar el cuestionario</a>'


def test():
    global last_question
    result = get_question_after(last_question, quiz)
    if result is None or len(result) == 0:   
            return redirect(url_for('result'))
    else:
        last_question = result[0]

    return f'<h1>Quiz: {quiz}<br>Pregunta: {result}</h1>'

def result():
    return '<h2>Resultado del test: (aqui mostramos el resultado)</h2>'


app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)


if __name__ == '__main__':
    app.run(debug='on')
