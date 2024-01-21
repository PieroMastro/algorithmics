#1. Media aritmética
def average(num1, num2, num3):
    print((num1 + num2 + num3)/3)

num1 = int(input('Ingrese un numero mayor a 0: '))
num2 = int(input('Ingrese un numero mayor a 0: '))
num3 = int(input('Ingrese un numero mayor a 0: '))

average(num1, num2, num3)

#2. Asistente matemático
def more(num1, num2):
    if num1 > num2:
        print('a es mayor que b')
    elif num2 > num1:
        print('a es menor que b')
    else:
        print('a es igual a b')


a = int(input("Ingresa un número para a:"))
b = int(input("Ingresa un número para b:"))
more(a, b)

#3. Ruta de turismo
def route(x, y):
    if y == 2:
        print('¡Acertó!')
    else:
        print('¡Falló!')

x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))
route(x, y)