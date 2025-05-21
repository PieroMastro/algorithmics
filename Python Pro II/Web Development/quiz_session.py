from flask import Flask, session, redirect, url_for
from queries_db import get_next_question
from random import randint


def index():
    max_quizzes = 3
    session['quiz'] = 1 #randint(1, max_quizzes) change to randint later
    session['prev_question'] = 0

    return "<h1>Hola Flask</h1><a href=/test>Click para iniciar!</a>"


def test():
    quiz = session['quiz']
    prev_question = session['prev_question']
    result = get_next_question(prev_question, quiz)

    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        session['prev_question'] = result[0]
        return f"<h2>Quiz: {session['quiz']}</h2><h3>Pregunta: {result}</h3>"


def result():
    return f"<h2>Resultado del Quiz {session['quiz']}:</h2>"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsSecret'
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run(debug=True)
