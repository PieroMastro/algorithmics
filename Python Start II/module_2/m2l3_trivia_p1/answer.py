from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton,  
    QPushButton, QLabel)


app = QApplication([])


# Panel de preguntas
button = QPushButton('Responder')
question = QLabel('¡La pregunta más difícil del mundo!')


radio_group_box = QGroupBox("Opciones de respuesta")


radio_btn1 = QRadioButton('Opción 1')
radio_btn2 = QRadioButton('Opción 2')
radio_btn3 = QRadioButton('Opción 3')
radio_btn4 = QRadioButton('Opción 4')


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(radio_btn1) # dos respuestas en la primera columna
layout_ans2.addWidget(radio_btn2)
layout_ans3.addWidget(radio_btn3) # dos respuestas en la segunda columna
layout_ans3.addWidget(radio_btn4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


radio_group_box.setLayout(layout_ans1)


# Crear un panel de resultados
answer_group_box = QGroupBox("Resultado de prueba")
result = QLabel('¿Es correcto o no?') # El texto de “Correcto” o “Incorrecto” estará aquí
correct = QLabel('¡Aquí estará la respuesta!') # el texto de respuesta correcta estará aquí 


answer_layout = QVBoxLayout()
answer_layout.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
answer_layout.addWidget(correct, alignment=Qt.AlignHCenter, stretch=2)
answer_group_box.setLayout(answer_layout)


# Colocar todos los widgets en la ventana:
layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultado de prueba
layout_line3 = QHBoxLayout() # botón de “Responder”


layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Colocar ambos paneles en la misma línea; uno estará escondido y el otro será mostrado:
layout_line2.addWidget(radio_group_box)   
layout_line2.addWidget(answer_group_box)  
radio_group_box.hide() # Ya hemos visto este panel; vamos a esconderlo y ver cómo quedó el panel de respuestas 


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


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')
window.show()


app.exec()
