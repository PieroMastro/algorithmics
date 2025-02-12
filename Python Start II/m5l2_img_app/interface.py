from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                            QPushButton, QLabel, QListWidget, QFileDialog)
import os

app = QApplication([])
main_win = QWidget()
main_win.resize(900, 600)
main_win.setWindowTitle('Image Editor App')

# WIDGETS
directory_btn = QPushButton('Carpeta')
images_list = QListWidget()

img_label = QLabel('Images')
btn_left = QPushButton('Izquierda')
btn_right = QPushButton('Derecha')
btn_mirror = QPushButton('Mirror')
btn_sharp = QPushButton('Nitidez')
btn_bw = QPushButton('B/N')

# LAYOUT
main_layout = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(directory_btn)
col_1.addWidget(images_list)

col_2 = QVBoxLayout()
col_2.addWidget(img_label, stretch=95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_mirror)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col_2.addLayout(row_tools)

main_layout.addLayout(col_1, stretch=20)
main_layout.addLayout(col_2, stretch=80)
main_win.setLayout(main_layout)


main_win.show()
app.exec_()