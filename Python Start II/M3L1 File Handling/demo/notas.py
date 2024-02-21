path = 'Python Start II/M3L1 File Handling/demo/notas.txt'

class Pupil():
    def __init__(self, surname, name, grades):
        self.surname = surname
        self.name = name
        self.grades = grades

best_students = []

with open(path, 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        data_pupil = Pupil(data[0], data[1], int(data[2]))
        
        if data_pupil.grades >= 4:
            best_students.append(data_pupil.surname)

print('Los mejores estudiantes de la clase son: ')

for student in best_students:
    print(student)





