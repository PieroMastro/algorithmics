'''Un módulo para calcular el resultado del test de Ruffier.

Idealmente, la suma de la frecuencia cardíaca debe ser medida en tres intentos:
(antes del ejercicio físico, inmediatamente después y después de un pequeño descanso)
no debe exceder más de 200 latidos por minuto.

Proponemos que los usuarios midan su pulso por 15 segundos 
y encuentren el resultado de latidos por minuto multiplicándolo por 4:

    S = 4 * (P1 + P2 + P3)

Mientras más lejano sea el resultado de los 200 latidos, peor es.
Tradicionalmente, las tablas son dadas por valores divididos entre 10. 

Índice de Ruffier: 
    IR = (S - 200) / 10

Es evaluado correspondiente a la edad según la tabla:
            7-8             9-10                11-12               13-14           15+ (adolescentes)
excel.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
bueno    >= 6.5 y < 12   >= 5 y < 10.5       >= 3.5 y < 9        >= 2 y < 7.5        >= 0.5 y < 6
satisf.  >= 12 y < 17    >= 10.5 y < 15.5    >= 9 y < 14         >= 7.5 y < 12.5     >= 6 y < 11
débil   >= 17 y < 21    >= 15.5 y < 19.5    >= 14 y < 18        >= 12.5 y < 16.5    >= 11 y < 15
Insatisf.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

para todas las edades, la diferencia entre los resultados débil e insatisfactorio es 4, 
la diferencia entre los resultados débil y satisfactorio es 5,
y la diferencia entre los resultados bueno y satisfactorio es 5.5

por lo tanto, vamos a programar la función ruffier_result(r_index, level) que recibiría
el índice de Ruffier calculado y el nivel "insatisfactorio" para la edad probada de la persona y retornará el resultado
'''

def ruffier_index(pulse_1:int, pulse_2:int, pulse_3:int):
    index = (4 * (pulse_1 + pulse_2 + pulse_3) - 200) / 10
    return round(index, 1)

