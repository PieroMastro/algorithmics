
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton, QPushButton,
    QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout)
    # importar nuevos metodos: QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout

app = QApplication([])

#INTERFAZ DE LA APP
# 1. Parametros de la app:
main_window = QWidget()
main_window.setWindowTitle('Notas inteligentes')
main_window.resize(900, 600)

# 2. Creando los widgets:
list_notes = QListWidget()
list_notes_label = QLabel('Lista de notas')
create_note_btn = QPushButton('Crear nota')
delete_note_btn = QPushButton('Borrar nota')
save_note_btn = QPushButton('Guardar nota')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Ingresar etiqueta...')
field_text = QTextEdit()
button_add = QPushButton('Añadir nota')
button_del = QPushButton('Remover etiqueta de nota')
button_search = QPushButton('Buscar notas por etiqueta')
list_tags = QListWidget()
list_tags_label = QLabel('Lista de etiquetas')

# 3. Organizando el diseño de los widgets:
notes_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(create_note_btn)
row_1.addWidget(delete_note_btn)
row_2 = QHBoxLayout()
row_2.addWidget(save_note_btn)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

notes_layout.addLayout(col_1, stretch = 2)
notes_layout.addLayout(col_2, stretch = 1)
main_window.setLayout(notes_layout)

# 4. Ejecutando la app:
main_window.show()
app.exec_()