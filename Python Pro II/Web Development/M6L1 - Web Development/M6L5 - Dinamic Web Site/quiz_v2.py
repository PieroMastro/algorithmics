# 1. Udpate imports
from random import randint
from flask import Flask, session, redirect, url_for, request 
from db_scripts import get_question_after, get_quizzes

# 2. Declare new functions
def start_quiz(quiz_id):
    session['quiz'] = quiz_id
    session['last_question'] = 0

def end_quiz():
    session.clear()

def quiz_form():
    # la función obtiene una lista de cuestionarios de la base de datos y crea un formulario con una lista desplegable

    html_top = f"""<html><body><h2>Elija un cuestionario:</h2><form method="POST" action="index"><select name="quiz">"""
    
    frm_submit = f"""<p><input type="submit" value="Seleccionar"> </p>"""
    
    html_end = f"""</select>{frm_submit}</form></body></html>"""
    
    options = ""
    
    q_list = get_quizzes()
    
    for id, name in q_list:
        option_line = f"""<option value="{id}">{name}</option>"""
        options += option_line
        
    return html_top + options + html_end

# 3. Update index function
def index():
    # Primera página: si vino con una solicitud GET, entonces elegir un cuestionario, si fue POST, entonces recordar el ID del cuestionario y enviarlo a las preguntas

    if request.method == 'GET':
        start_quiz(-1)
        return quiz_form()

    else:
        quiz_id = request.form.get('quiz')
        start_quiz(quiz_id)
        return redirect(url_for('test'))

# 4. Update test function
def test():
    # Devuelve la página de la pregunta
    # ¿Qué ocurriría si un usuario sin elegir un cuestionario fuera directo a la dirección '/test'?
    if "quiz" not in session or int(session["quiz"]) < 0:
        return redirect(url_for("index"))
    else:
        # Todavía hay una versión antigua de la función:
        result = get_question_after(session["last_question"], session["quiz"])
        if result is None or len(result) == 0:
            return redirect(url_for("result"))
        else:
            session["last_question"] = result[0]
            # Si hemos enseñado a la base de datos a devolver Row o dict, entonces no debemos escribir result[0] y en su lugar escribimos result['id']
            return f"<h1>{session['quiz']}<br>{result}</h1>"

    
def result():
    return "<h2>Cuestionario completado!</h2>"

# Crear un objeto de aplicación web:
app = Flask(__name__) 
app.add_url_rule('/', 'index', index) # crea una regla para la URL '/'
app.add_url_rule('/index', 'index', index, methods=['POST', 'GET']) # regla para '/index'
app.add_url_rule('/test', 'test', test) # crea una regla para la URL '/test'
app.add_url_rule('/result', 'result', result) # crea una regla para la URL '/test'

# Establecer la clave de encriptación:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
    # Iniciar el servidor web:
    app.run()
