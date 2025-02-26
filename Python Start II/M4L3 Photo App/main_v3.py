from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                            QPushButton, QLabel, QListWidget, QFileDialog)
from PIL import Image, ImageFilter
import os

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
        pixmap_img = QPixmap(path)
        width, height = img_label.width(), img_label.height()
        pixmap_img = pixmap_img.scaled(width, height, Qt.KeepAspectRatio)
        img_label.setPixmap(pixmap_img)
        img_label.show()
        
    def change_to_bw(self):
        if self.image:
            self.image = self.image.convert('L')
            self.save_image()
            image_path = os.path.join(self.directory, self.save_directory, self.filename)
            self.show_image(image_path)
        
    def save_image(self):
        path = os.path.join(self.directory, self.save_directory)
        if not os.path.exists(path):
            os.mkdir(path)
            
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

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

# APP LOGIC
work_directory = ''
current_img = ImageProcessor()

def choose_work_directory():
    global work_directory
    work_directory = QFileDialog.getExistingDirectory()
    print(f'Folder: {work_directory}')

def filter(filenames, extensions):
    result = []
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
                break # para salir del bucle interno si se encuentra una coincidencia
    return result

def show_filenames_list():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    filenames = filter(os.listdir(work_directory), extensions)
    images_list.clear()
    for pic in filenames:
        images_list.addItem(pic)

def show_chose_img():
    if images_list.currentRow() >= 0:
        filename = images_list.currentItem().text()
        current_img.load_image(work_directory, filename)
        image_path = os.path.join(work_directory, current_img.filename)
        current_img.show_image(image_path)


# EVENT HANDLINg
directory_btn.clicked.connect(choose_work_directory)
directory_btn.clicked.connect(show_filenames_list)

images_list.currentRowChanged.connect(show_chose_img)
btn_bw.clicked.connect(current_img.change_to_bw)

app.exec_()
