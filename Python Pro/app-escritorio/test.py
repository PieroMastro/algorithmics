from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLineEdit
)
from instructions import *
from result import ResultWindow


class TestWindow(QWidget):
    def __init__(self, title=TXT_TEST_TITLE):
        super().__init__()
        self.title = title

        self.set_ui()
        self.config_win()
        self.connections()
        self.show()

    def set_ui(self):
        # TODO: Crear los elementos gráficos para recopilar datos:
        # 1. QLineEdit para edad, P1, P2 y P3
        # 2. QPushButton para iniciar temporizadores y enviar resultados
        # 3. Organizar los elementos en QVBoxLayout y QHBoxLayout
        pass

    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def connections(self):
        # TODO: Conectar el botón de enviar resultados con el método self.next_click
        pass

    def next_click(self):
        # TODO: Instanciar ResultWin (pasando los datos ingresados) y ocultar esta ventana
        pass
