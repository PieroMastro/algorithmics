# AUTOMATIZACION 2 (2-4)

def get_course(wish):
    if wish.find('deportes') != -1:
        course = 'voleibol'
    elif wish.find('ciencias') != -1:
        course = 'astronomía'
    elif wish.find('cómics') != -1:
        course = 'bocetos'
    else:
        course = 'historia de la Roma antigua'
    return course

num_estudiantes = int(input('Número de estudiantes:'))

for i in range(num_estudiantes):
    wish = input('Ingresa tu deseo:')

    if get_course(wish) != 'astronomía':
        print('Recomendado:', get_course(wish))
    else:
        print('Recomendado:', get_course(wish))
        print('¡Advertencia! ¡Las clases se realizan en la noche!')


