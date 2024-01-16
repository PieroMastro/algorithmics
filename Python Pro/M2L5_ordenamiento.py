lista = list(map(int, input('Ingrese numero separados por espacios: ').split()))
print(lista)

indice_menor = 0
numero_menor = lista[0]


for i in range(1, len(lista)):
    if lista[i] < numero_menor:
        indice_menor = i
        numero_menor = lista[i]
lista[indice_menor] = lista[0]
lista[0] = numero_menor
print(lista)


