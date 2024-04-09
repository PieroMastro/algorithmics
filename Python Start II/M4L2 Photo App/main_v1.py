# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 1.0 | os integration/main functionality          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
import os

app = QApplication([])
# 1. App params
window = QWidget()
window.setWindowTitle('Photo Editor App')
window.resize(700, 400)

# 2. Widgets
folder_btn = QPushButton('Carpeta')
files_list = QListWidget()

img_label = QLabel('Image')
left_btn = QPushButton('Izquierda')
right_btn = QPushButton('Derecha')
flip_btn = QPushButton('Reflejo')
sharp_btn = QPushButton('Nitidez')
bn_btn = QPushButton('B/N')

# 3. Layout
main_layout = QHBoxLayout()
left_col = QVBoxLayout()
right_col = QVBoxLayout()

# left side
left_col.addWidget(folder_btn)
left_col.addWidget(files_list)

# right_side
buttons = QHBoxLayout()
buttons.addWidget(left_btn)
buttons.addWidget(right_btn)
buttons.addWidget(flip_btn)
buttons.addWidget(sharp_btn)
buttons.addWidget(bn_btn)
right_col.addWidget(img_label)
right_col.addLayout(buttons)

main_layout.addLayout(left_col, 20)
main_layout.addLayout(right_col, 80)
window.setLayout(main_layout)

window.show()


# 4. Functionality
# seleccionando el directorio
def choose_workdir():
    global workdir
    workdir =QFileDialog.getExistingDirectory()

# filtrando archivos de imagenes
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

# mostrando lista de archivos
def show_filenames_list():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    choose_workdir()
    filenames = filter(os.listdir(workdir), extensions)
    files_list.clear()
    for filename in filenames:
        files_list.addItem(filename)


folder_btn.clicked.connect(show_filenames_list)

app.exec_()