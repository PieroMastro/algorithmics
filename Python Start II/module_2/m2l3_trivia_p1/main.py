from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                            QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                            QGroupBox, QRadioButton, QButtonGroup, QPushButton, QLabel)


app = QApplication([])


question = QLabel('¡La pregunta más difícil del mundo!')
button = QPushButton('Responder')

# Panel de preguntas (botones de radio)
question_group_box = QGroupBox("Opciones de respuesta")
radio_btn1 = QRadioButton('Opción 1')
radio_btn2 = QRadioButton('Opción 2')
radio_btn3 = QRadioButton('Opción 3')
radio_btn4 = QRadioButton('Opción 4')

radio_group = QButtonGroup()
radio_group.addButton(radio_btn1)
radio_group.addButton(radio_btn2)
radio_group.addButton(radio_btn3)
radio_group.addButton(radio_btn4)

questions_layout = QHBoxLayout()   
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
col_1.addWidget(radio_btn1) # dos respuestas en la primera columna
col_1.addWidget(radio_btn2)
col_2.addWidget(radio_btn3) # dos respuestas en la segunda columna
col_2.addWidget(radio_btn4)

# Agregando las columnas al layout de preguntas
questions_layout.addLayout(col_1)
questions_layout.addLayout(col_2)

# Estableciendo el layout en el contenedor de preguntas
question_group_box.setLayout(questions_layout)


# Panel de resultados (respuesta)
answer_group_box = QGroupBox("Resultado de prueba")
result = QLabel('Resultado de la respuesta (Correcto o Incorrecto)')
correct_answer = QLabel('Aquí estará la respuesta correcta')


answer_layout = QVBoxLayout()
answer_layout.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
answer_layout.addWidget(correct_answer, alignment=Qt.AlignHCenter, stretch=2)
answer_group_box.setLayout(answer_layout)


# Colocar todos los widgets en la ventana:
layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultado de prueba
layout_line3 = QHBoxLayout() # botón de “Responder”


layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# Colocar ambos paneles en la misma línea; uno estará escondido y el otro será mostrado:
layout_line2.addWidget(question_group_box)   
layout_line2.addWidget(answer_group_box)
answer_group_box.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2) # el botón debería ser grande
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # los espacios entre el contenido

def show_result():
    question_group_box.hide() # Panel de preguntas oculto para visualizar el de respuesta
    answer_group_box.show()
    button.setText('Siguiente Pregunta')

def show_question():
    question_group_box.show()
    answer_group_box.hide()
    button.setText('Responder')
    radio_group.setExclusive(False)
    radio_btn1.setChecked(False)
    radio_btn2.setChecked(False)
    radio_btn3.setChecked(False)
    radio_btn4.setChecked(False)
    radio_group.setExclusive(True)

def start_test():
    if button.text() == "Responder":
        show_result()
    else:
        show_question()

button.clicked.connect(start_test)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Questionario App')
window.resize(480, 300)
window.show()


app.exec()
