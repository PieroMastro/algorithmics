# ORDENAMIENTO POR SELECCION

checklist =  list(map(int, input("Ingresa los elementos de la lista separados por espacios: ").split()))
print(checklist)

# 1. ENCONTRAR EL NUMERO MAS PEQUEÑO DE NUESTRA LISTA:
minimal_value = checklist[0]

for numero in checklist:
    if numero <= minimal_value:
        minimal_value = numero
print(minimal_value)

# 2. RECORDAR EL NUMERO MAS PEQUEÑO Y SU INDICE EN LA LISTA:

for i in range(len(checklist)):
    if checklist[i] <= minimal_value:
        minimal_index = i
        minimal_value = checklist[i]
print(minimal_value)
print(minimal_index)

# 3. CAMBIAR LOS VALORES LUEGO DE ENCONTRAR EL NUMERO MAS PEQUEÑO Y ASIGNARLO AL 1ER INDICE:
minimal_value = checklist[0]
minimal_index = 0
for i in range(1, len(checklist)):
    if checklist[i] <= minimal_value:
        #nuevo numero mas pequeno y su indice
        minimal_index = i
        minimal_value = checklist[i]
#aqui cambiamos su valor
checklist[minimal_index] = checklist[0]
checklist[0] = minimal_value
print(checklist)

# 4. IMPLEMENTAR CICLOS ANIDADOS PARA QUE NUESTRO ALGORITMO DE ORDENAMIENTO SE REPITA,
#  HASTA QUE TENGAMOS LA LISTA CON TODOS LOS ELEMENTOS REEMPLAZADOS DE MENOR A MAYOR.

for j in range(len(checklist) - 1):
    minimal_index = j
    minimal_value = checklist[j]
    for i in range(j + 1, len(checklist)):
        if checklist[i] < minimal_value:
            minimal_index = i
            minimal_value = checklist[i]
    checklist[minimal_index] = checklist[j]
    checklist[j] = minimal_value
print(checklist)

