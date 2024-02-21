demo = 'Python Start II/M3L1 File Handling/demo/demo.txt'

with open(demo, 'r', encoding='utf-8') as file:
    for line in file:
        print(line)

author = input('¿Quién escribió el poema?: ')
with open(demo, 'a', encoding='utf-8') as file:
    file.write(f'\n({author})')

while True:
    question = input('¿Quieres agregar otro poema?: ')
    question = question.lower()

    if question == 'si':
        poem = input('Ingrese el poema: ')
        author = input('Ingrese el autor: ')
        with open(demo, 'a', encoding='utf-8') as file:
            file.write(f"{poem}\n({author})\n")
    else:
        break

print("Contenido actualizado del archivo:")
with open(demo, "r", encoding="utf-8") as file:
    for line in file:
        print(line)
