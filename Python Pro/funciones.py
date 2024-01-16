def invertir_texto(texto):
    texto_invertido = ""
    count = len(texto) - 1
    while count >= 0:
        texto_invertido = texto_invertido + texto[count]
        count = count - 1
    print(texto_invertido)


print('''
Este es un programa para cifrar y descifrar oraciones.
Seleccione lo que desea hacer e ingrese el número correspondiente:
1 - cifrado por inversión. Los datos de entrada son una cadena. El resultado es una cadena;
2 - cifrado 'cortar-pegar'. Los datos de entrada son una cadena. El resultado es una lista;
3- descifrado del texto cifrado usando el método por inversión. Los datos de entrada son una cadena. El resultado es una cadena;
4 - descifrado del texto cifrado usando el método 'cortar-pegar'. Los datos de entrada son una cadena. El resultado es una cadena;
Para salir, ingrese -1.
''')
question = int(input("¿Qué quieres hacer?  "))
while question != -1:
    if question == 1:
        str1 = input("Ingresa tu texto: ")
        invertir_texto(str1)
        question = int(input("¿Qué quieres hacer?  "))
    elif question == 2:
        str1 = input("Ingresa tu texto: ")
        invertir_texto(str1)
        question = int(input("¿Qué quieres hacer?  "))