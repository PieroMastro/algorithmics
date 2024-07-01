from time import time
import questions
import test


name = input("Por favor, escribe tu nombre: ")

welcome = f'Bienvenido {name}, esta es una app simple de preguntas y respuestas \nPor favor seleciona la respuesta correcta (1, 2, 3 o 4)\n'
print(welcome)

#inicio de la cuenta regresiva del tiempo
start_time = time()  


#llamada a la función de prueba
point = test.check_question(questions.question1)
point = point + test.check_question(questions.question2)
point = point + test.check_question(questions.question3)
point = point + test.check_question(questions.question4)
point = point + test.check_question(questions.question5)


#fin de la cuenta regresiva del tiempo
end_time = time()


#recuento del tiempo dedicado a la prueba
result_time = end_time - start_time
result_time = round(result_time,2)


#llamada de función con la comprobación de resultados
estimation = test.estimation(point)


#salida de los resultados de la prueba
print('\n')
print(f'Felicidades {name}!')
print('Puntos obtenidos:', point)
print(f'Te tomo: {result_time} seg completar la prueba')
print(estimation)