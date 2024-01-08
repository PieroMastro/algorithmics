from time import time

# CRONOMETRO:
stopwatch = input('1 - iniciar, 0 - detener: ')

while stopwatch != '0':
    if stopwatch == '1':
        start = time()
    else:
        stopwatch = input('Ingrese 1 para iniciar: ')
    stopwatch = input('0 - detener: ')

end = time()
total = end-start
print('Tiempo total:', round(total, 2), 'seg')