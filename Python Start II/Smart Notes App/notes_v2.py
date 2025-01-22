
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                            QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog)
                            # importar nuevos metodos: QListWidget, QLineEdit, QTextEdit, QInputDialog
import json

app = QApplication([])

# NOTAS EN JSON
# Ya no hay necesidad de declarar nuestro archivo json, las funciones que creamos se encargan de 
# notes = {
#     "¡Bienvenido!" : {
#         "texto" : "¡Esta es la mejor app para tomar notas del mundo!",
#         "etiquetas" : ["Bien", "Instrucciones"]
#     }
# }
# with open("notes_data.json", "w") as file:
#     json.dump(notes, file, ensure_ascii=False)

#INTERFAZ DE LA APP
# 1. Parametros de la app:
main_window = QWidget()
main_window.setWindowTitle('App de Notas Inteligentes')
main_window.resize(900, 600)

# 2. Creando los widgets:
list_notes = QListWidget()
list_notes_label = QLabel('Lista de Notas')
create_note_btn = QPushButton('Crear Nota')  # al presionarlo debe aparecer una ventana emergente con el campo "Ingresar nombre de Nota"
delete_note_btn = QPushButton('Borrar Nota')
save_note_btn = QPushButton('Guardar Nota')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Ingresar Etiqueta...')
field_text = QTextEdit()
button_add = QPushButton('Añadir Nota')
button_del = QPushButton('Remover Etiqueta de Nota')
button_search = QPushButton('Buscar Notas por Etiqueta')
list_tags = QListWidget()
list_tags_label = QLabel('Lista de Etiquetas')

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


# FUNCIONALIDAD DE LA APP

# Obtener el texto de la nota con el título resaltado y mostrarlo en el campo de editar
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["texto"])
    list_tags.clear()
    list_tags.addItems(notes[key]["etiquetas"])
    
# Agregar una nueva nota
def add_note():
    note_name, ok = QInputDialog.getText(main_window, 'Agregar Nota', 'Nombre de la Nota')
    if ok and note_name != '':
        notes[note_name] = {
            'texto': '',
            'etiquetas': []
        }

        list_notes.addItem(note_name)
        #list_tags.addItems(notes[note_name]['etiquetas'])
        print(notes)

# Eliminar una nota
def delete_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)

        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)

    else:
        print('Por favor seleccione una nota para eliminar!')

# Guardar una nota
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['texto'] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Por favor seleccione una nota para guardar!')


# 4. Ejecutando la app:
# Procesamiento de evento de eventos
create_note_btn.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
save_note_btn.clicked.connect(save_note)
delete_note_btn.clicked.connect(delete_note)

main_window.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()
