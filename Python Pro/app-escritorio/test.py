from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instructions import *


class TestWin(QWidget):
    def __init__(self, title=TXT_TITLE):
        super().__init__()
        self.title = title

        self.set_ui()
        self.config_win()
        self.show()

    def set_ui(self):
        self.label = QLabel("Segunda ventana")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.label, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def connections(self):
        pass
