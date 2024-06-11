# Tarea 3.  Obtener el texto de la pregunta y opciones de respuestas

def get_question_after(question_id = 0, quiz_id=1):
    ''' devuelve la siguiente pregunta después de la pregunta con el ID pasado
    para la primera pregunta, se pasa el valor predeterminado '''
    open()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id '''
    cursor.execute(query, [question_id, quiz_id] )
    result = cursor.fetchone()
    close()
    return result