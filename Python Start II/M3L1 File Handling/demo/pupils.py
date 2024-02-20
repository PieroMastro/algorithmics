pupils = 'Python Start II/M3L1 File Handling/demo/pupils.txt'

class Pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

best_students = []

with open(pupils, 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(" ")
        data_pupil = Pupil(data[0], data[1], int(data[2]))

        if data_pupil.mark >= 4:
            best_students.append(data_pupil.surname)

print("Los mejores estudiantes son:")
for student in best_students:
    print(student)
