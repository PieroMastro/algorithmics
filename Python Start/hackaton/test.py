
#la función de prueba. Devuelve el número de respuestas correctas
def check_question(question):
    last_letter = question.find("#")
    cut_question = question[0: last_letter]
    right_answer = question[last_letter +1 ]
    answer = input(cut_question)

    if answer == right_answer:
        return 1
    else:
        return 0


#la función de verificar los resultados de la prueba. Comprueba si el participante ha superado la prueba
def estimation(point):
    if point < 2 :
        return "No lograste responder la mitad de las respuestas correctamente."
    elif point > 4:  
        return "¡¡Has pasado la prueba con excelente score!!"
    else :  
        return "¡Practica un poco más y vuelve!"