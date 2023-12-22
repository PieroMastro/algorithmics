# La longitud de la lista y todos los elementos en una columna

lista = input('entrar en una lista').split()
print(len(lista))
count = 0

while count < len(lista):
    print(lista[count])
    count += 1

# Concatenación y duplicación de listas

lista_1 = input('Entrar en la primera lista:').split()
lista_2 = input('Entrar en la segunda lista:').split()

print(lista_1 + lista_2)
print(lista_1 * 3)
print(lista_2 * 3)

# Añadiendo elementos a listas

B = ["python", "es", "genial"]
B.append('@coding.py')
print(B)

# Convirtiendo cadenas de una lista en números

lista = input('entrar en una lista').split()
lista = list(map(int, lista))
print(lista)

# Reemplazando separadores

lista = input('entrar en una lista').split()
separador = 'PY'
print(separador.join(lista))

# Lista secreta

lista = input('entrar en una lista').split()
lista = lista + lista * 3
print('I*T'.join(lista))

# Todo número par

lista = input('entrar en una lista').split()
count = 0

while count < len(lista):
    print(lista[count])
    count += 2

# Coordenadas del punto de encuentro

a = input("Entrar en una lista: ").split()
a = list(map(int, a))
count = 0
pares = False  # Variable para verificar si se encontró al menos un número par
while count < len(a):
    if a[count] % 2 == 0:
        print(a[count])
        pares = True
    count += 1
if not pares:
    print(-1)

# Mayor que el anterior

lista = list(map(int, input('Entrar en una lista: ').split()))

count = 1  # Comenzamos desde el segundo elemento, ya que no hay un elemento anterior para el primero

while count < len(lista):
    if lista[count] > lista[count - 1]:
        print(lista[count])
    count += 1
