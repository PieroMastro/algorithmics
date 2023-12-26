# CIFRADO CESAR:

text = input('Ingrese una cadena de texto:')
shift = 3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]
print('plain text:', text)
print('encrypted text:', encrypted_text)

# 1.1 DEFINIDO CON FUNCION:

text = input('Ingrese un texto a encriptar: ')
shift = input('Ingrese un numero (entre 1 y 26): ')

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)