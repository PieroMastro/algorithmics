numero = int(input('Ingrese un numero: '))
total = 0
for number in range(1, numero + 1):
    total += number
    print(number)
print(f'La suma de los numeros 1 hasta el {numero} = {total}')
