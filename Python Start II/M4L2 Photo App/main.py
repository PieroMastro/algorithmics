from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

#INTERFAZ DE LA APP
# 1. Parametros de la app:
window = QWidget()
window.setWindowTitle('Editor Simple')
window.resize(700, 400)

# 2. Elementos de la Interfaz:
# col1
folder_btn = QPushButton('Carpeta')
files_list = QListWidget()
# col2
img_label = QLabel('Imagen')
left_btn = QPushButton('Izquierda')
right_btn = QPushButton('Derecha')
flip_btn = QPushButton('Reflejo')
sharp_btn = QPushButton('Nitidez')
bn_btn = QPushButton('B/N')

main_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

col_1.addWidget(folder_btn)
col_1.addWidget(files_list)
col_2.addWidget(img_label, 95)

row_buttons = QHBoxLayout()
row_buttons.addWidget(left_btn)
row_buttons.addWidget(right_btn)
row_buttons.addWidget(flip_btn)
row_buttons.addWidget(sharp_btn)
row_buttons.addWidget(bn_btn)
col_2.addLayout(row_buttons)

main_layout.addLayout(col_1, 20)
main_layout.addLayout(col_2, 80)
window.setLayout(main_layout)

window.show()
app.exec()