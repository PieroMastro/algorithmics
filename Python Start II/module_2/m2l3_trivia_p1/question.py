from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)


app = QApplication([])


window = QWidget()
window.setWindowTitle('Trivia')


### Interfaz para la aplicación de Trivia ###

button = QPushButton('Responder') # botón de responder
question = QLabel('¿En qué año se lanzó el juego Super Mario 64?') # texto de pregunta


radio_btn_box = QGroupBox("Opciones de respuesta") # grupo en la pantalla para botones de radio con respuestas
radio_btn1 = QRadioButton('1998')
radio_btn2 = QRadioButton('2001')
radio_btn3 = QRadioButton('1996')
radio_btn4 = QRadioButton('2010')


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # los verticales estarán dentro de los horizontales
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(radio_btn1) # dos respuestas en la primera columna
layout_ans2.addWidget(radio_btn2)
layout_ans3.addWidget(radio_btn3) # dos respuestas en la segunda columna
layout_ans3.addWidget(radio_btn4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # las columnas están en la misma línea


radio_btn_box.setLayout(layout_ans1) # el “panel” con opciones de respuesta está listo 


layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultados de prueba
layout_line3 = QHBoxLayout() # botón de “Responder”


layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(radio_btn_box)


layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2) # el botón debería ser grande
layout_line3.addStretch(1)


# Ahora vamos a colocar las líneas que hemos creado una debajo de la otra:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # los espacios entre el contenido


window.setLayout(layout_card)
window.show()
app.exec()
