import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(500, 100, 300, 400)

        font = QFont("Arial", 18)  # Seleccionar fuente y tamaño
        self.setFont(font)  # Aplicar fuente a la ventana

        self.input_field = QLineEdit(self)
        self.input_field.setFixedHeight(80)
        self.input_field.setFont(QFont("Arial", 28))  # Aplicar fuente al campo de entrada
        self.input_field.setStyleSheet("background-color: #f2f2f2; border: 1px solid #ccc;")  # Aplicar fondo personalizado
        self.input_field.setAlignment(Qt.AlignRight)  # Alinear texto a la derecha

        buttons_layout = QVBoxLayout()
        button_labels = [
            ['1', '2', '3', '/', '√'],
            ['4', '5', '6', '*', '%'],
            ['7', '8', '9', '-', '+/-'],
            ['C', '0', '.', '=', '+']
        ]

        for row in button_labels:
            row_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.clicked.connect(self.on_button_click)
                button.setFont(QFont("Arial", 18))  # Aplicar fuente a los botones
                row_layout.addWidget(button)
            buttons_layout.addLayout(row_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_field)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def on_button_click(self):
        button = self.sender()
        if button.text() == 'C':
            self.input_field.clear()
        elif button.text() == '=':
            try:
                result = eval(self.input_field.text())
                self.input_field.setText(str(result))
            except Exception as e:
                self.input_field.setText("Error")
        elif button.text() == '.':
            if '.' not in self.input_field.text():
                self.input_field.setText(self.input_field.text() + '.')
        elif button.text() == '√':
            try:
                result = eval(self.input_field.text()) ** 0.5
                self.input_field.setText(str(result))
            except Exception as e:
                self.input_field.setText("Error")
        elif button.text() == '%':
            try:
                result = eval(self.input_field.text()) / 100
                self.input_field.setText(str(result))
            except Exception as e:
                self.input_field.setText("Error")
        elif button.text() == '+/-':
            try:
                result = -eval(self.input_field.text())
                self.input_field.setText(str(result))
            except Exception as e:
                self.input_field.setText("Error")
        else:
            self.input_field.setText(self.input_field.text() + button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())