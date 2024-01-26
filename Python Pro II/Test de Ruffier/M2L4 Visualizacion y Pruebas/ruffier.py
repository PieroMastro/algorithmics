'''Un módulo para calcular el resultado del test de Ruffier.

Idealmente, la suma de la frecuencia cardíaca debe ser medida en tres intentos (antes del ejercicio físico, inmediatamente después y después de un pequeño descanso)
no debe exceder más de 200 latidos por minuto. 
Proponemos que los niños midan su pulso por 15 segundos 
y encuentren el resultado de latidos por minuto multiplicándolo por 4:
    S = 4 * (P1 + P2 + P3)
Mientras más lejano sea el resultado de los 200 latidos, peor es.
Tradicionalmente, las tablas son dadas por valores divididos entre 10. 

Índice de Ruffier   
    IR = (S - 200) / 10
es evaluado correspondiente a la edad según la tabla:
            7-8             9-10                11-12               13-14               15+ (¡solo para adolescentes!)
excel.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
bueno    >= 6.5 y < 12   >= 5 y < 10.5       >= 3.5 y < 9        >= 2 y < 7.5        >= 0.5 y < 6
satisf.  >= 12 y < 17    >= 10.5 y < 15.5    >= 9 y < 14         >= 7.5 y < 12.5     >= 6 y < 11
débil   >= 17 y < 21    >= 15.5 y < 19.5    >= 14 y < 18        >= 12.5 y < 16.5    >= 11 y < 15
Insatisf.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

para todas las edades, la diferencia entre los resultados débil e insatisfactorio es 4, 
la diferencia entre los resultados débil y satisfactorio es 5 y la diferencia entre los resultados bueno y satisfactorio es 5.5

por lo tanto, vamos a programar la función ruffier_result(r_index, level) que recibiría
el índice de Ruffier calculado y el nivel "insatisfactorio" para la edad probada de la persona y retornará el resultado
'''
# aquí puedes especificar las cadenas que representan el resultado:
txt_index = "Tu Índice de Ruffier: "
txt_workheart = "Rendimiento cardíaco: "
txt_nodata = '''no hay datos para esta edad'''
txt_res = [] 
txt_res.append('''bajo. ¡Ve a ver a tu doctor de inmediato!''')
txt_res.append('''satisfactorio. ¡Consulta tu doctor!''')
txt_res.append('''promedio. 
Tal vez valga la pena hacerse unas pruebas adicionales con el doctor.''')
txt_res.append('''más alto que el promedio''')
txt_res.append('''alto''')

def ruffier_index(P1, P2, P3):
    '''retorna el valor del índice según los tres cálculos de pulso para su comparación con la tabla'''
    pass

def neud_level(age):
    '''las opciones con una edad menor que 7 y con adultos deben ser procesadas por separado; 
    aquí seleccionamos el nivel “insatisfactorio” solo dentro de la tabla:
    para la edad de 7, “insatisfactorio” es un índice de 21, luego en adelante cada 2 años disminuye en 1.5 hasta el nivel de 15 a los 15-16 años '''
    pass
    
def ruffier_result(r_index, level):
    '''la función obtiene el índice de Ruffier y lo interpreta 
    retornando el nivel de preparación: un número del 0 al 4
    (mientras más alto el nivel de preparación, mejor).'''
    pass

def test(P1, P2, P3, age):
    '''esta función puede ser usada fuera del módulo para calcular el índice de Ruffier.
    Retorna los textos terminados que serán colocados en el lugar correcto
    Para los textos, usa las constantes especificadas al inicio del módulo.'''
    pass
