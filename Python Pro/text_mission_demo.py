print('''     
Este es un juego de misiones, para superarlo debes elegir entre múltiples respuestas.
¡Ten cuidado y buena suerte!
''')
 
print('''
Para seleccionar una respuesta, elige la letra correspondiente
''')
 
print('''
Estabas caminando por el bosque con tus amigos cuando se encontraron con una choza abandonada.
Decidir ingresar en ella no fue lo mejor - la choza estaba maldita. ¡Tus amigos han sido secuestrados y sólo tú puedes rescatarlos!
''')
 
answer_1 = input('''
Tienes unas llaves y una pequeña navaja en tus manos.
Frente a ti hay una antigua puerta de madera.
¿Qué haces?
 
a - intentar romper la puerta
b - intentar abrirla con las llaves
c - intentar forzarla con la navaja
d - buscar otra opción''')
 
if answer_1 == "a":
    print('''
La puerta no cedió.
Debes buscar otro camino, es una pena haber perdido el tiempo.
''')
elif answer_1 == "b":
    print('''
Las llaves se rompieron, no fue una buena idea.
''')
elif answer_1 == "c":
    print('''
Fruto de la desesperación, no es posible.
Por desgracia, la puerta está cerrada y la navaja se ha roto.
''')
else:
    print('''
La puerta se ve muy sólida, lo mejor es buscar otro camino.
''')
 
answer_2 = input('''
Mirando alrededor notas una ventana cerrada. El pestillo está del otro lado, pero hay un espacio bastante amplio.
Quizás podrías intentar levantar el pestillo con la navaja.
 
a - intentar levantar el pestillo con la navaja
b - romper el vidrio con tu hombro
c - tratar de aflojar el marco de la ventana
d - pedir ayuda
''')
 
if answer_2 == "a":
    print('''
Luego de unos minutos de tormento, eres capaz de levantar el pestillo.
La ventana está abierta, ahora puedes salir de la casa.
''')
elif answer_2 == "b":
    print('''
No es la mejor idea. El vidrio no cederá y te dolerá el hombro por un momento.
Lo mejor es usar la navaja.
''')
elif answer_2 == "c":
    print('''
Tras media hora, es obvio que esta no es la mejor idea. El marco, si bien es viejo, es sólido y no cederá.
Prueba con la navaja.
''')
else:
    print('''
Tras media hora de gritar, has fallado.
Tienes que salir por tu cuenta.
Es hora de usar la navaja. 
''')
 
answer_3 = input('''
Saliste de la casa. Encuentras unas extrañas llaves en el suelo bajo la ventana.
Cerca de la casa encuentras una cabina donde tus amigos están encerrados.
¡Debes rescatarlos!
La cabina es vieja y temblorosa.
Hay una enorme cerradura colgando de la puerta.
¿Qué haces?
 
a - tratar de romper la cerradura con la navaja
b - sacudir la cabina
c - tratar de abrir la cerradura con las llaves que encontraste
d - tratar de romper la puerta con tu pie
''')
 
if answer_3 == "a":
    print('''
No fue una acción exitosa el intentar romper una cerradura con una navaja
de mano, pero valía la pena intentarlo.
Desafortunadamente, no obtuviste ningún resultado.
''')
elif answer_3 == "b":
    print('''
Parece ser que la cabina era muy endeble.
Tan sólo un pequeño toque bastó para hacerla rodar a un acantilado con tus amigos en ella.
''')
elif answer_3 == "c":
    print('''
Es muy fácil, pero funcionó.
Las llaves abrieron la cerradura y todos están libres.
''')
else:
    print('''
Parece ser que la cabina era muy endeble.
El impacto la rompió y la hizo caer rodando hacia un acantilado, donde por inercia fuiste a parar tú también.
''')

