from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton, QPushButton,
    QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout)
    # importar nuevos metodos: QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout
import json

app = QApplication([])

#NOTAS EN JSON
# No es necesario escribir el json file al inicio, lo manejamos a travez de funcionex vinculadas a los botones ahora

# notes = {
#     'Bienvenido!' : {
#         'texto' : 'Esta es la mejor app para tomar notas!',
#         'etiquetas' : ['Accion 1', 'Accion 2', 'Accion 3']
#     }
# }

# with open('notes_data.json', 'w') as file:
#     json.dump(notes, file, ensure_ascii=False)

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

#FUNCIONALIDAD DE LA APP
# trabajando con el texto de la nota
def add_note():
    # utilizamos la ventana QInputdialog y creamos un elemento de notas, guardando en list_notes
    note_name, ok = QInputDialog.getText(
        main_window, "Añadir nota", "Nombre de nota: "
    )
    if ok and note_name != "":
        notes[note_name] = {
            'texto' : '',
            'etiquetas' : []
        }
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['etiquetas'])
        print(notes)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['texto'] = field_text.toPlainText()
        
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii=False)
            print(notes)
    else:
        print('¡Ninguna nota seleccionada!')

def del_note():
    # eliminamos la nota del diccionario y limpia los datos de la nota en los widgets:
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)

        with open('notes_data.json', 'w', encoding='utf') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
            print(notes)
    else:
        print('¡Ninguna nota seleccionada!')

def show_note():
# obtener el texto de la nota con el título resaltado y mostrarlo en el campo de editar:
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["texto"])
    list_tags.clear()
    list_tags.addItems(notes[key]["etiquetas"])

# trabajando con las etiquetas de la nota:
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['etiquetas']:
            notes[key]['etiquetas'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open('notes_data.json', 'w', encoding= 'utf-8') as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
        print(notes)
    else:
        print('Debe seleccionar una nota para agregar una etiqueta!')

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['etiquetas'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['etiquetas'])
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print('La etiqueta a eliminar no ha sido seleccionada')

def search_tag():
    print(button_search.text())

    tag = field_tag.text()

    if button_search.text() == 'Buscar notas por etiqueta' and tag:
        print(tag)
        # las notas con la etiqueta resaltada se amacenan aqui:
        notes_filtered = {}

        for note in notes:
            if tag in notes[note]['etiquetas']:
                notes_filtered[note] = notes[note]
        
        button_search.setText('Restablecer busqueda')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_search.text())
    
    elif button_search.text() == 'Restablecer busqueda':
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_search.setText("Buscar notas por etiqueta")
        print(button_search.text())
    else:
        pass


# manejo de eventos:
list_notes.itemClicked.connect(show_note)
create_note_btn.clicked.connect(add_note)
save_note_btn.clicked.connect(save_note)
delete_note_btn.clicked.connect(del_note)
button_add.clicked.connect(add_tag)
button_del.clicked.connect(del_tag)
button_search.clicked.connect(search_tag)

# 4. Ejecutando la app:
main_window.show()

# mostrar el archivo json:
with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()