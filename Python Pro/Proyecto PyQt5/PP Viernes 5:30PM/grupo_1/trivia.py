from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import randint, shuffle


class Question():
    # contiene una pregunta, una respuesta correcta y tres incorrectas

    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []
questions_list.append(
    Question('¿El Idioma oficial de Brasil?', 'Portugués', 'Inglés', 'Español', 'Brasilero'))
questions_list.append(
    Question('¿Qué color no aparece en la bandera americana?', 'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(
    Question('¿Cuál no es una estructura de datos en Python?', 'String', 'Lista', 'Tupla', 'Diccionario'))
questions_list.append(
    Question('¿Cuál de los siguientes no es un Pokemon?', 'Bumblebee', 'Charizard', 'Pikachu', 'Ditto'))
questions_list.append(
    Question('¿Cuantos continentes existen?', '7', '6', '5', '4'))
questions_list.append(
    Question('¿Cuál de los siguientes no es un peleador de Street Fighter?', 'Kyo', 'Ken', 'Vega', 'Urien'))
questions_list.append(
    Question('¿Cuál animal tiene más de un corazón?', 'Pulpo', 'Lemur', 'Caracol', 'Cangrejo'))


app = QApplication([])


btn_OK = QPushButton('Reply')  # el botón responder
lb_Question = QLabel('¡La pregunta más difícil del mundo!')  # texto de la pregunta


RadioGroupBox = QGroupBox("Opciones de respuesta")  # grupo en pantalla de botones radio


rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


RadioGroup = QButtonGroup()  # este es un grupo de botones radio para controlar su comportamiento
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()  # guías verticales dentro de una horizontal
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)  # opciones de dos respuestas en la primera columna
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)  # Dos opciones de respuesta en la segunda columna
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)  # columnas colocadas en línea


RadioGroupBox.setLayout(layout_ans1)  # el "panel" con opciones de respuesta está listo


AnsGroupBox = QGroupBox("Resultados de la prueba")
lb_Result = QLabel('are you right or not?')  # aquí se escribirá si está en lo cierto o equivocado
lb_Correct = QLabel('¡La respuesta estará aquí!')  # here will be the text of the correct answer


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()  # pregunta
layout_line2 = QHBoxLayout()  # Opciones de respuesta o resultado de prueba
layout_line3 = QHBoxLayout()  # "Botón "Responder"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()  # ocultar el panel de respuestas, el panel de preguntas primero debe ser visible
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # el botón debe ser grande


layout_line3.addStretch(1)

layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # espacios entre los elementos del contenido


def show_result():
    ''' mostrar el panel de opiniones '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Próxima pregunta')


def show_question():
    ''' mostrar panel de pregunta '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Respuesta')
    RadioGroup.setExclusive(False)  # se eliminaron las restricciones para restablecer la opción de botón radio
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # devolvió las restricciones, ahora solo se puede seleccionar un botón de opción


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' la función escribe los valores de la pregunta y las respuestas en los widgets correspondientes,
    al mismo tiempo, las opciones de respuesta se distribuyen aleatoriamente'''
    shuffle(answers)  # se mezcló la lista de botones, ahora algún botón al azar es el primero en la lista.
    answers[0].setText(q.right_answer)  # rellenar el primer elemento de la lista con la respuesta correcta, el resto con las incorrectas
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)  # pregunta
    lb_Correct.setText(q.right_answer)  # respuesta
    show_question()  # mostrar el panel de preguntas


def show_correct(res):
    " mostrar el resultado - establecer el texto pasado a la inscripción resultado y mostrar el panel que necesitamos "
    lb_Result.setText(res)
    show_result()


def check_answer():
    'si se elige cualquier opción de respuesta, tenemos que comprobar y mostrar el panel de respuesta'


    if answers[0].isChecked():
        # ¡respuesta correcta!
        show_correct('¡Correcto!')
        window.score += 1
        print('Estadísticas\n-Preguntas totales: ', window.total, '\n-Preguntas correrctas: ', window.score)
        print('CaIificación: ', (window.score / window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # ¡Respuesta incorrecta
            show_correct('¡Respuesta incorrecta!')
            print('CaIificación: ', (window.score / window.total * 100), '%')


def next_question():
    'hace una pregunta aleatoria desde la lista'
    window.total += 1
    print('Estadísticas\n-Preguntas totales: ', window.total, '\n-Preguntas correrctas: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # no necesitamos el valor anterior,
    # ¡esto significa que pueden usar una variable local!
    # elegido aleatoriamente una pregunta en la lista
    # si introduce unas cien palabras, rara vez se repetirán
    q = questions_list[cur_question]  # se eligió una pregunta
    ask(q)  # hace pregunta


def click_OK():
    'determina si se muestra otra pregunta o se comprueba la respuesta a ésta.'


    if btn_OK.text() == 'Respuesta':
        check_answer()  # chequeo de respuesta
    else:
        next_question()  # siguiente pregunta


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')

btn_OK.clicked.connect(click_OK)  # al pulsar el botón, elegimos qué ocurre exactamente

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()