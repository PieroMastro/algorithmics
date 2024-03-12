from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton, QPushButton,
    QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout)
    # importar nuevos metodos: QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout
import json

app = QApplication([])
notes = []

#NOTAS EN JSON
# No es necesario escribir el json file al inicio, lo manejamos a travez de funciones vinculadas a los botones ahora

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

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

def add_note():
    # utilizamos la ventana QInputdialog y creamos un elemento de notas, guardando en list_notes
    note_name, ok = QInputDialog.getText(
        main_window, "Añadir nota", "Nombre de nota: "
    )
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
        print(notes)
    else:
        print("¡La nota para guardar no está seleccionada!")


# manejo de eventos:
list_notes.itemClicked.connect(show_note)
create_note_btn.clicked.connect(add_note)
save_note_btn.clicked.connect(save_note)


# 4. Ejecutando la app:
main_window.show()

# mostrar notas:
name = 0
note = []
while True:
    #leyendo y añadiendo 
    filename = str(name)+".txt"
    try:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
        
        notes.append(note)
        note = []
        name += 1
    
    # manejo de excepciones cuando no se encuentra la nota
    except IOError:
        break

print(notes)
for note in notes:
    list_notes.addItem(note[0])

app.exec_()