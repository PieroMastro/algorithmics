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
