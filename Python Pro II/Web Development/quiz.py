def quiz_form():
    # 1. Obtener la lista de cuestionarios
    # Asumimos que get_quises() devuelve una lista de tuplas/listas (id, nombre)
    q_list = get_quizzes()

    # 2. Construir las opciones del desplegable de manera eficiente
    options_html_parts = []
    for quiz_id, quiz_name in q_list:
        # Usamos f-string para interpolar los valores de forma limpia
        options_html_parts.append(f'<option value="{quiz_id}">{quiz_name}</option>')

    # Unimos todas las partes de las opciones en una sola cadena
    options_html = "\n".join(options_html_parts) # Añadimos un salto de línea para legibilidad del HTML

    # 3. Ensamblar el HTML completo usando f-strings
    # La URL de la acción del formulario debe ser una ruta válida en tu Flask app, ej. "/select_quiz"
    # Cambié 'index' a '/select_quiz' como un ejemplo más descriptivo
    full_html = f'''
        <!DOCTYPE html>
        <html>
            <body>
                <h2>Elija un cuestionario:</h2>
                <form method="post" action="/select_quiz">
                    <select name="quiz">
                        {options_html}
                    </select>
                    <p><input type="submit" value="Seleccionar"></p>
                </form>
            </body>
        </html>
        '''
    return full_html
