from flask import Flask, session, redirect, url_for
from db_scripts import get_next_question

app = Flask(__name__)

def index():
    session['quiz'] = 1
    session['current_question'] = 0

    return "<h1>Bienvenido a la app de cuestionarios!</h1><a href=/test>Click para iniciar!</a>"


def test():
    quiz = session['quiz']
    current_question = session['current_question']
    result = get_next_question(current_question, quiz)

    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        session['current_question'] = result[0]
        return f"<h2>Quiz: {session['quiz']}</h2><h3>Pregunta: {result}</h3>"


def result():
    return f"<h2>Resultado del Quiz {session['quiz']}:</h2>"


app.config['SECRET_KEY'] = 'ThisIsSecret'
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run(debug=True)
