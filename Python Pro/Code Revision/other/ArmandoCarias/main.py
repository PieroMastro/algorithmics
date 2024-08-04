# Historia inicial
print('''Hace tiempo, dos razas gobernaban la Tierra: Humanos y Mounstros.
Un día, una guerra se desató entre las dos razas.
Tras una larga batalla, los humanos salieron victoriosos.
Sellaron a los mounstros bajo tierra con un hechizo mágico.
Muchos años más tarde... En el MT. EBOTT 201X
Las leyendas cuentan que aquellos que escalan la montaña nunca regresan.
Un niño cae del precipicio, cayendo en el agujero que lleva al lugar donde ahora están los monstruos.
''')


# Función para obtener la respuesta según el nombre
def get_response(name):
    responses = {
        "toriel": "Creo que deberías pensar en tu propio nombre, mi niño.",
        "sans": "nope",
        "flowey": "Yo ya he ELEGIDO ese nombre.",
        "asgore": "No puedes.",
        "asriel": "...",
        "undyne": "¡Consigue tu PROPIO nombre!",
        "alphys": "N-no hagas eso.",
        "papyrus": "¡¡¡¡NO LO PERMITO HUMANO!!!!",
        "temmie": "oLI!",
        "mettaton": "¡¡¡OOOOH!!! ¿ESTÁS PROMOCIONANDO MI MARCA?",
        "chara": "El nombre verdadero."
    }
    return responses[name]


# Pedir nombre al jugador
while True:
    name = input('''Nombra al humano caido: ''').lower()
    if name in ["toriel", "sans", "flowey", "asgore", "asriel", "undyne", "alphys", "papyrus", "temmie", "mettaton", "chara"]:
        print(get_response(name))
    else:
        break

    
# Continuar con la historia
print('''
Para tu suerte sobreviviste el impacto y te encuestras con una Flor''')

print('''-¡Buenas! Soy Flowey. ¡Flowey la flor! Hmmm...
-Eres nuevo en el subsuelo, ¿a que sí?
-Caramba, debes de estar muy confuso.
-¡Alguien debería enseñarte cómo funcionan las cosas aquí!
-Supongo que ese tendré que ser yo.

-Por aquí abajo el AMOR se comparte,
-para hacer fuerte a tu alma que es la culminación de tu propio ser debes conseguir mucho AMOR
-Quieres algo de AMOR, ¿no? No te preocupes, compartiré un poco contigo! *guiña el ojo*
-El AMOR se comparte con estas "pequeñas bolitas de amistad". ¡Agarra todas las que puedas!
''')

# Preguntar al jugador qué hacer
while True:
    answer1 = int(input(''' 
    1 - Agarrarlas
    2 - Moverte
    >>> '''))

    if answer1 == 1:
        print('''*intentado agarrar las balas te dejan muy herrido
        -Idiota. En este mundo es matar o morir
        -¡¿Por que iría alguien a dejar pasar una oportunidad como esta?!''')
        break

    elif answer1 == 2:
        print('''*te mueves y esquivas las bolitas de amistad
        -Oye Amigo, no has agarrado ni una.
        -Probemos otra vez, ¿vale?
        *las vuelves a esquivar*
        -¿Es una broma? ¿Eres tonto? VE. HACIA. LAS. ¡¡BALAS!!
        -digo... bolitas de amistad.
        *las vuelves a esquivar*
        ...
        -Parece que ya sabes lo que está pasando aquí, ¿eh?
        -Y que solo quieres verme sufrir.''')
        break

# Continuar con la historia
print('''*Te rodea con más balas
    -MUERE.

    ...

    *Un mounstro te salva y tira a Flowey

    -Qué criatura tan terrible, torturando a una alma tan joven e inocente.
    -Ah, no tengas miedo, mi niño. Soy Toriel, la guardiana de las Ruinas.
    -Paso por este lugar todos los días para ver si alguien ha caído.
    -Eres el primer humano que llega en mucho tiempo. ¡Ven! Te guiaré por las catacumbas.

    *Entran a una sala con un maniquí

    -Como humano que vive en el subsuelo, los mounstros te atacarán.
    -Deberías estar preparado para tal situación.
    -¡Ahora bien no te preocupes! El proceso es simple.
    -Cuando te encuentres con un mounstro entrarás en una lucha.
    -Mientras estes en la lucha entabla una conversación amistosa.
    -Gana tiempo, vendré a resolver el conflicto. Practica hablando con el maniquí
    ''')

answer2 = int(input('''*Te has topado con el Maniquí.

    1 - Luchar
    2 - Hablar
    3 - Perdonar
    4 - Huir
    >>> '''))

if answer2 == 1:
    print('''
    *Le haces daño al cuerpo del Maniquí y muere desvaneciendose
    *¡HAS GANADO!
    *Consigues 0 AMOR.
    ''')
elif answer2 == 2:
    print('''
    *Hablas con el Maniquí.
    ...
    *No se ve que tenga muchas ganas de charlar.
    *Toriel parece feliz contigo.
    *¡HAS GANADO!
    *Consigues 0 AMOR.
    ''')

elif answer2 == 3:
    print('''
    *El Maniquí está cansado de tu diatriba sin sentido
    *¡HAS GANADO!
    *Consigues 0 AMOR.
    ''')

else:
    print('''
    Escapas...
    ''')