from flask import Flask, session


def index():
    """ Al visitar el sitio, restablecemos el contador y brindamos un enlace a la página con el cambio del contador """
    session['counter'] = 0
    return '<a href="/counter">Next</a>'

def counter():
    """ Aumentar el contador y dar un enlace a la página con el cambio del contador """
    session['counter'] += 1
    return '<h1>' + str(session['counter']) + '</h1>'


# Crear un objeto de aplicación web:
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'VeryStrongKey'
app.add_url_rule('/', 'index', index) # crea una regla para la URL '/':
app.add_url_rule('/counter', 'counter', counter) # crea una regla para la URL 'counter/'

if __name__ == '__main__':
    # Iniciar el servidor web:
    app.run()