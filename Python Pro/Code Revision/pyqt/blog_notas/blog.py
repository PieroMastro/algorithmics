from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                            QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit,
                            QMessageBox)
from PyQt5.QtCore import Qt


with open('notes.txt','w') as file:
    file.write('PRUEBA')
    file.close()

# FUNCIONALIDAD
# Funcion para cargar una nota:
def open_note():
    pass

# Funcion para salvar una nota:
def save_note():
    pass

# CONSTANTES
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 600


# MAIN WINDOW
app = QApplication([])
main_window = QWidget()
main_window.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
main_window.setWindowTitle("Notes App")

main_window.show()


# WIDGETS
nota_text_edit = QTextEdit()
crear_nota_button = QPushButton("Crear nota")
abrir_nota_button = QPushButton("Abrir nota")
guardar_nota_button = QPushButton("Guardar nota")


# LAYOUT
layout_botones = QHBoxLayout()
layout_botones.addWidget(crear_nota_button)
layout_botones.addWidget(abrir_nota_button)
layout_botones.addWidget(guardar_nota_button)

layout_principal = QVBoxLayout()
layout_principal.addLayout(layout_botones)
layout_principal.addWidget(nota_text_edit)

main_window.setLayout(layout_principal)








app.exec_()
