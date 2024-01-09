# IMPORTAR MODULOS
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel

# CREAR APP Y LA VENTANA PRINCIPAL:
# Creamos una instancia de la clase QApplication, y la ventana principal (Qwidget), la inicializamos con los metodos .
app = QApplication([])
window = QWidget()
window.setWindowTitle('Tarjeta de Memoria')
window.resize(400, 300)

# ESTABLECER LOS ELEMENTOS DE LA INTERFACE:
question = QLabel('¿Que Nacionalidad no existe?') # texto de pregunta
ok_button = QPushButton('Respuesta') # botón de responder

# CREACION DE LOS BOTONES DE RADIO Y AGRUPARLOS CON QGroupBox:
RadioGroupButton = QGroupBox('Opciones de respuesta')
rbt1 = QRadioButton('Enets')
rbt2 = QRadioButton('Pitufos')
rbt3 = QRadioButton('Chulyms')
rbt4 = QRadioButton('Aleutas')

# DEFINIENDO LAYOUTS, SE CREA UNO HORIZONTAL Y 2 VERTICALES (PARA ANIDARLOS EN EL HORIZONTAL)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # los verticales estarán dentro de los horizontales
layout_ans3 = QVBoxLayout()

# ESTABLECER LOS BOTONES EN SUS RESPECTIVOS LAYOUTS (VERTICALES):
layout_ans2.addWidget(rbt1) # dos respuestas en la primera columna
layout_ans2.addWidget(rbt2)
layout_ans3.addWidget(rbt3) # dos respuestas en la segunda columna
layout_ans3.addWidget(rbt4)

# ANIDAMOS LOS LAYOUTS VERTICALES AL HORIZONTAL:
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # las columnas están en la misma línea

# ESTRABLECER EL LAYOUT PARA EL GRUPO DE BOTONES:
RadioGroupButton.setLayout(layout_ans1) # panel con opciones de respuesta completado

# DEFINICION DEL LAYOUT PRINCIPAL (en 3 lineas horizontrales para organizar los elementos):
layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta
layout_line3 = QHBoxLayout() # botón de respuesta

# INCORPORACION DE LOS WIDGETS A LOS LAYOUTS:
layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) # centramos vertical y horizontal con el parametro alignment
layout_line2.addWidget(RadioGroupButton)
layout_line3.addStretch(1)
layout_line3.addWidget(ok_button, stretch=3) # con el parametro stretch controlamos el tamaño relativo de nuestro boton
layout_line3.addStretch(1)

# CREANDO NUESTRO LAYOUT VERTICAL PRIMARIO (e incorporamos nuestro 3 layouts horizontales):
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # espacio entre el contenido

# ESTABLECIENDO NUESTRP MAIN LAYOUT EN LA VENTANA:
window.setLayout(layout_card)

# MOSTRAR E INICIALIZAR LA APP
window.show()
app.exec_()
