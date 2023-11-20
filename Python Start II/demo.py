# Construir una nueva clase, generar numero aleatorio
import random

class GeneradorAleatorio():
    def __init__(self, numero_minimo, numero_maximo):
        self.numero_minimo = numero_minimo
        self.numero_maximo = numero_maximo

    def generar(self):
        return random.randint(self.numero_minimo, self.numero_maximo)

generador = GeneradorAleatorio(1, 100)
numero_aleatorio = generador.generar()
print(numero_aleatorio)
