from entrenamiento import *

informacion()

pregunta = input('¿Cómo puedo ayudarte?: (off - salida) ')

while pregunta != 'off':
    if pregunta == '1':
        mostrar_horario()
    elif pregunta == '2':
        mostrar_entrenador()
    else:
        print('Ingrese una opcion valida')
    input('¿De qué otra forma puedo ayudarte?: (off - salida) ')

