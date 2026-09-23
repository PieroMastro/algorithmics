from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from test import TestWin


class MainWindow(QWidget):
    def __init__(self, title=TXT_TITLE):
        super().__init__()
        self.title = title

        self.set_ui()
        self.config_win()
        self.conections()
        self.show()

    def set_ui(self):
        # Elementos gráficos
        self.hello_text = QLabel(TXT_HELLO)
        self.instruction = QLabel(TXT_INSTRUCTION)
        self.btn_next = QPushButton(TXT_NEXT, self)

        # Configuración del layout
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.layout_line)

    def config_win(self):
        # Dimensiones y posición
        self.setWindowTitle(self.title)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def conections(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.test = TestWin()  # Instancia de la clase que referencia la 2da ventana
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
