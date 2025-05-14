from flask import Flask, session

counter = 0
app = Flask(__name__)
app.config['SECRET_KEY'] = 'superclavesecreta'

def index():
    global counter
    counter = 0
    # session['counter'] = 0
    return f'<a href=/counter>Next</a>'

def counter():
    global counter
    counter += 1
    # session['counter'] += 1
    # return f'<h1>Counter: {session["counter"]}</h1>'
    return f'<h1>Counter: {counter}</h1>'


app.add_url_rule('/', 'index', index)
app.add_url_rule('/counter', 'counter', counter)

if __name__ == '__main__':
    app.run(debug='on')
