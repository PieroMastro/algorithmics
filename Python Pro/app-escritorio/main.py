from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from instructions import *
from test import TestWindow


class MainWindow(QWidget):
    def __init__(self, title=TXT_TITLE):
        super().__init__()
        self.title = title

        self.set_ui()
        self.config_win()
        self.connections()
        self.show()

    def set_ui(self):
        # Elementos gráficos
        self.hello_text = QLabel(TXT_HELLO)
        self.instruction = QLabel(TXT_INSTRUCTION)
        self.btn_next = QPushButton(TXT_NEXT, self)

        # Layout principal
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.layout_line)

    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def connections(self):
        # TODO: Conectar el clic de self.btn_next con el método self.next_click
        pass

    def next_click(self):
        # TODO: Instanciar la clase TestWin, ocultar la ventana actual (self.hide())
        pass


if __name__ == '__main__':
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
