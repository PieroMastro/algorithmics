'''1. Crear una funcion que pida un texto,
    valide si es un palindromo (sin tomar en cuenta los espacios)
    y retorneun booleano'''

def check_palindrome(text: str) -> bool:
    text.replace(" ", "").lower()
    return text == text[::-1]

