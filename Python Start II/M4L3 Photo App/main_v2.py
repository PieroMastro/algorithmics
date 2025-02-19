# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 2.0 | photo file choose and show in app          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
import os

app = QApplication([])
# 1. App params
window = QWidget()
window.setWindowTitle('Photo Editor App')
window.resize(800, 600)

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
left_col.addWidget(files_list, 95)

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
# class para manejar el procesamiento de imagenes
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.directory = None
        self.save_directory = 'modificado/'
    
    def load_image(self, directory, filename):
        self.directory = directory
        self.filename = filename
        image_path = os.path.join(directory, filename)
        self.image = Image.open(image_path)

    def show_image(self, path):
        img_label.hide()
        pixmap_img = QPixmap(path)
        width, height = img_label.width(), img_label. height()
        pixmap_img = pixmap_img.scaled(width, height, Qt.KeepAspectRatio)
        img_label.setPixmap(pixmap_img)
        img_label.show()

# Creando una instancia de la clase ImageProcessor
work_img = ImageProcessor()
curent_img = ImageProcessor()

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

# seleccionar las imagenes
def show_chose_img():
    if images_list.currentRow() >= 0:
        filename = images_list.currentItem().text()
        current_img.load_image(work_directory, filename)
        image_path = os.path.join(work_directory, current_img.filename)
        current_img.show_image(image_path)

folder_btn.clicked.connect(show_filenames_list)
images_list.currentRowChanged.connect(show_chose_img)
files_list.clicked.connect(show_choosen_img)

app.exec_()
