# La palabra más corta

line = input("Ingresa una cadena: ")
words = line.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("La palabra más corta: " + str(shortest))
print("La longitud de la palabra más corta: " + str(len(shortest)))

# Clave

lista = input('Ingresa una cadena:').split()
codigo = ''

for palabra in lista:
    codigo += str(len(palabra))
print(codigo)

# Cuadrados de números

numero = int(input('Ingrese un numero > 0'))
total = 0

for num in range(1, numero + 1):
    total += num ** 2
print(total)

# Misión

lista_equipos = list(map(int, input().split()))

for i in range(len(lista_equipos)):
    if lista_equipos[i] % 2 == 0:
        print(i)

# Búsqueda en una cadena

texto = input()
palabras = texto.split() # separamos cada palabra de la cadena de texto en una lista

palabra_mas_corta = palabras[0]
palabra_mas_larga = palabras[0]

for palabra in palabras:
    if len(palabra) < len(palabra_mas_corta):
        palabra_mas_corta = palabra
    elif len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print(palabra_mas_larga, palabra_mas_corta)

# Números factoriales

numero = int(input('Ingrese un numero no negativo:'))
total = 1

if numero == 0 or numero == 1:
    print(total)
else:
    for i in range(2, numero + 1):
        total = total * i
    print(total)

# ejemplo

numero = int(input('Ingrese un numero: '))
total = 0
for number in range(1, numero + 1):
    total += number
    print(number)
print(f'La suma de los numeros 1 hasta el {numero} = {total}')
