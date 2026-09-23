from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instructions import *


class ResultWindow(QWidget):
    def __init__(self, exp=None, title=TXT_RESULT_TITLE):
        super().__init__()
        self.title = title
        self.exp = exp  # Recibe la información del usuario/evaluación si es necesario

        self.set_ui()
        self.config_win()
        self.connections()
        self.show()

    def set_ui(self):
        # TODO: Crear las etiquetas QLabel para mostrar el Índice de Ruffier y el Rendimiento Cardíaco
        self.index_label = QLabel(TXT_INDEX)
        self.result_label = QLabel(TXT_WORKOUT)

        # TODO: Crear un QVBoxLayout, agregar los widgets alineados al centro y establecer el layout
        self.layout_line = QVBoxLayout()
        # self.layout_line.addWidget(...)
        
        self.setLayout(self.layout_line)

    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def connections(self):
        # En esta ventana no hay botones de navegación
        pass
