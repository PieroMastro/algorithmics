# ORDENAMIENTO POR SELECCION

checklist =  list(map(int, input("Ingresa los elementos de la lista separados por espacios: ").split()))
print(checklist)

# 1. ENCONTRAR EL NUMERO MAS PEQUEÑO DE NUESTRA LISTA:

minimal_value = checklist[0]

for i in checklist:
    if i <= minimal_value:
        minimal_value = i
print(minimal_value)

# 2. RECORDAR EL NUMERO MAS PEQUEÑO Y SU INDICE EN LA LISTA:

minimal_value = checklist[0]
minimal_index = 0

for i in range(len(checklist)):
    if checklist[i] <= minimal_value:
        minimal_index = i
        minimal_value = checklist[i]
print(minimal_value)
print(minimal_index)

# 3. CAMBIAR LOS VALORES LUEGO DE ENCONTRAR EL NUMERO MAS PEQUEÑO Y ASIGNARLO AL 1ER INDICE:

for i in range(1, len(checklist)):
    if checklist[i] < minimal_value:
        minimal_index = i
        minimal_value = checklist[i]

checklist[minimal_index] = checklist[0]
checklist[0] = minimal_value
print(checklist)