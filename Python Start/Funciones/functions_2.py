# FUNCIONES ANIDADAS

def get_result(score):
    if score >= 85:
        return '1er lugar'
    elif score >= 65 and score < 85:
        return '2do lugar'
    elif score >= 50 and score < 65:
        return '3er lugar'
    else:
        return '¡Mejor suerte la próxima vez!'


score = int(input('Ingresar puntaje:'))
print('Tu resultado:', get_result(score))


# CALCULO DE RENDIMIENTO

def control_rating(rating):
   if 65 <= rating <= 100:
       print('Rendimiento académico dentro de lo normal.')
   else:
       print('¡Rendimiento académico bajo!')
 

def set_loop(num):
    for i in range(num):
        rating = int(input('Puntaje:'))
        control_rating(rating)

num_repeticiones = int(input('Ingrese el numero de calificaciones a consultar: '))

set_loop(num_repeticiones)

