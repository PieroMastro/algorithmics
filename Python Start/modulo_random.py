import random
from random import *

# numero_aleatorio = randint(1, 1000000)
# print(numero_aleatorio)
# numero_aleatorio = random()
# numero_2_decimales = round(numero_aleatorio, 2)
# print(numero_2_decimales)

# PROGRAMA PARA CALCULAR SORTEO DE EQUIPOS ALEATORIAMENTE:
# total = int(input('El numero de equipos: '))
# participant_1 = randint(1, total)
# participant_2 = randint(1, total)

# print(f'Equipo {participant_1} vs Equipo {participant_2}')

#PROGRAMA PARA CALCULAR DISTRIBUCION DE JUGADORES A LOS EQUIPOS DE MANERA ALEATORIA:
name = input('Nombre de la persona (off - finalizar): ')

while name != 'off':
    equipo = randint(1,2)
    print(name, ', equipo', equipo)
    name = input('Nombre de la persona (off - finalizar): ')
print('Equipos completados')


