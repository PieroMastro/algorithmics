# Importando módulos y widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit

# Declarando constantes
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
POS_X, POS_Y = 200, 200
TEXT_TITLE = "Enviando texto"
TXT_SEND = "Enviar"
TXT_LINE = "Campo de entrada"


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        # Llamando a un constructor de la clase padre
        super().__init__(parent=parent, flags=flags)

    # Creando y personalizando los elementos gráficos
        self.initUI()

        # Conecta los elementos
        self.connects()

        # Determina cómo se verá la ventana (texto, tamaño, ubicación)
        self.set_appear()

        # Inicio:
        self.show()

    def initUI(self):
        # Creando elementos graficos
        self.btn_send = QPushButton(TXT_SEND, self)
        self.line = QLineEdit(TXT_LINE)
        self.lable_finish = QLabel()

        self.layout_line = QHBoxLayout()
        self.layout_line.addWidget(self.line, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_send, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.lable_finish, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

    def next_click(self):
        self.lable_finish.setText(self.line.text())

    def connects(self):
        self.btn_send.clicked.connect(self.next_click)

    # Determina posicion/tamaño y caracteristicas de la vebtana
    def set_appear(self):
        self.setWindowTitle(TEXT_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.move(POS_X, POS_Y)

def main():
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

main()