from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt


app = QApplication([])
main_window = QWidget()
main_window.resize(800, 600)

main_window.setWindowTitle("app")

main_window.show()
#main_window.hide()

file = open('notes.txt', 'w')
file.write('Información')
file.close()
texto = QLabel("Hello World!", alignment = Qt.AlignCenter)


boton = QPushButton("presionar")

texto.hide()
v_line.addWidget(texto)
v_line.addWidget(boton)

file.hide()
v_line.addWidget(file)



def show_fun_title():
    texto.show()

def mostrar_escrito():
    file.show()






main_window.setLayout(v_line)
boton.clicked.connect(show_fun_title)

app.exec_()
