super_cadena = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
var1 = 2
var2 = 'variables'

# STRING FORMANTING
# print(f'Ejemplo de concatenacion utilizando {var1} {var2}')



# # LEN: devuelve la longitud de la cadena (cuantos caracteres tiene, incluyendo espacios).
# cantidad_elementos = len(cadena)

# # CORTE DE UNA CADENA: cadena[a,b] retorna una subcadena que inicia desde el primer parametro (que corresponde al indice) y termina en el segundo, si se omite el ultimo argumento se extiende al final de la cadena.
# indice = cadena[3]
# corte = cadena[3: 21]
# print(indice, corte)

# # SPLIT: divide una cadena de texto en partes más pequeñas utilizando un separador.
# palabras = cadena.split(" ")  # Divide la frase en palabras usando el espacio como separador

# # FIND: busca un patrón específico en una cadena y devuelve el índice de la primera ocurrencia. Si no encuentra el patrón, retorna -1.
# indice = cadena.find("jugar")
# print(indice)


# # RFIND: Similar a find(), pero busca desde la derecha y devuelve el índice de la última ocurrencia.
# ultima_o = cadena.rfind("o")
# print("La ultima o se encuentra en el indice:", ultima_o)

# # REPLACE: reemplaza todas las ocurrencias de una subcadena con otra subcadena en una cadena.
# mensaje = "Hola, mundo!"
# nuevo_mensaje = mensaje.replace("mundo", "Python")
# print(nuevo_mensaje)
# print(super_cadena.replace('Lorem', 'Hola'))

# super_cadena.count('Lorem')
# # COUNT: cuenta cuántas veces aparece un valor específico en una lista o cadena.

cantidad_lorem = super_cadena.count('Lorem')
print(cantidad_lorem)