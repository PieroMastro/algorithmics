from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # todas las líneas deben ser dadas durante la creación del objeto y serán registradas como propiedades
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.questions_list = []



questions_list = [] 
questions_list.append(Question('El idioma nacional de Brasil', 'Portugués', 'Brasilero', 'Español', 'Italiano'))
questions_list.append(Question('¿Qué color no aparece en la bandera de Estados Unidos?', 'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(Question('Una residencia tradicional de los yakutos', 'Urasa', 'Yurta', 'Iglú', 'Choza'))


app = QApplication([])


button = QPushButton('Responder') # botón de responder
question_label = QLabel('¡La pregunta más difícil del mundo!') # texto de pregunta


radio_group_box = QGroupBox("Opciones de respuesta") # grupo en pantalla para los botones de radio con respuestas


rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


radio_group = QButtonGroup() # este agrupa los botones de radio para poder controlar su comportamiento
radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # las verticales estarán dentro de la horizontal 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # dos respuestas en la primera columna
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # dos respuestas en la segunda columna
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # colocar las columnas en la misma línea


radio_group_box.setLayout(layout_ans1) # un “panel” está listo con las opciones de respuesta 


answer_group_box = QGroupBox("Resultado de prueba")
result_label = QLabel('¿Es correcto o no?') # la palabra “correcto” o “incorrecto” estará escrita aquí
correct_label = QLabel('Aquí está la respuesta correcta') # el texto de la respuesta correcta estará aquí


layout_res = QVBoxLayout()
layout_res.addWidget(result_label, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct_label, alignment=Qt.AlignHCenter, stretch=2)
answer_group_box.setLayout(layout_res)


layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultado de prueba
layout_line3 = QHBoxLayout() # botón “Responder”


layout_line1.addWidget(question_label, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(radio_group_box)   
layout_line2.addWidget(answer_group_box)  
answer_group_box.hide() # esconde el panel de respuesta porque el panel de preguntas debe ser visible primero 


layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2) # el botón debe ser grande
layout_line3.addStretch(1)


card_layout = QVBoxLayout()

card_layout.addLayout(layout_line1, stretch=2)
card_layout.addLayout(layout_line2, stretch=8)
card_layout.addStretch(1)
card_layout.addLayout(layout_line3, stretch=1)
card_layout.addStretch(1)
card_layout.setSpacing(5) # espacios entre los contenidos


def show_result():
    # Mostrar el panel de respuesta
    radio_group_box.hide()
    answer_group_box.show()
    button.setText('Siguiente pregunta')


def show_question():
    # Mostrar el panel de pregunta
    radio_group_box.show()
    answer_group_box.hide()
    button.setText('Responder')
    # limpia el botón de radio seleccionado
    radio_group.setExclusive(False) # remueve los límites para poder reiniciar los botones de radio 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True) # reinicia los límites para que solo un botón de radio pueda ser seleccionado a la vez 


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(question: Question):
    # Esta función escribe el valor de la pregunta y respuestas en los widgets correspondientes. Las opciones de respuesta son distribuidas aleatoriamente
    shuffle(answers) # coloca los botones de la lista en orden aleatorio
    answers[0].setText(question.right_answer) # llena el primer elemento de la lista con la respuesta correcta y los otros elementos con respuestas incorrectas
    answers[1].setText(question.wrong1)
    answers[2].setText(question.wrong2)
    answers[3].setText(question.wrong3)
    question_label.setText(question.question) # pregunta
    correct_label.setText(question.right_answer) # respuesta
    show_question() # muestra panel de pregunta 


def show_correct(res):
    # Mostrar el resultado, colocar el texto que fue pasado a esta función en la etiqueta de “resultado” y mostrar el panel relevante
    result_label.setText(res)
    show_result()


def check_answer():
    # Si una de las opciones de respuesta es seleccionada, comprobarla y mostrar el panel de respuesta.
    if answers[0].isChecked():
        # respuesta correcta
        show_correct('¡Correcto!')
        window.score += 1   
        print('Estadísticas\n-Preguntas totales: ', window.total, '\n-Preguntas correctas: ', window.score)
        print('Calificación:', round((window.score / window.total * 100), 2), '%')
    else:
        # if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        # respuesta incorrecta
        show_correct('¡Incorrecto!')
        print('Calificación:', round((window.score / window.total * 100), 2), '%')


def next_question():
    window.total += 1
    # Realiza la siguiente pregunta en la lista de manera aleatoria.
    # esta función necesita una variable que dé el número de la pregunta actual 
    # window.current_question = window.current_question + 1 # pasa a la siguiente pregunta NO SE NECESITA
    current_question = randint(0, len(questions_list) - 1)
    # if window.current_question >= len(questions_list):
    #     window.current_question = 0 # si la lista de preguntas ha terminado, se vuelve a comenzar 
    question = questions_list[current_question] # toma una pregunta
    ask(question) # pregunta


def click_button():
    # Esto determina si se muestra otra pregunta o se comprueba la respuesta a esta pregunta.
    if button.text() == 'Responder':
        check_answer() # comprueba la respuesta
    else:
        next_question() # siguiente pregunta


window = QWidget()
window.setLayout(card_layout)
window.setWindowTitle('Trivia App')
window.resize(400, 300)
# Hace la pregunta actual de la lista, una propiedad del objeto “ventana”.
# De esa forma, podemos cambiar fácilmente sus funciones:
# window.current_question = -1    # idealmente, las variables como esta deberían ser propiedades 
                                # tendríamos que escribir una clase cuyas instancias tengan estas propiedades,
                                # pero Python nos permite crear una propiedad para una sola instancia 

window.score = 0
window.total = 0

button.clicked.connect(click_button) # cuando se hace clic en un botón, escogemos exactamente lo que sucede 

# Todo está preparado. Ahora hacemos la pregunta y mostramos la ventana:
next_question()
window.show()

app.exec()
