# ====================================================
#          PROYECTO 1 | MISION DE TEXTO             
# ====================================================

print('''====================================================
          LA CABAÑA DE LOS SUSURROS                
====================================================
Este es un juego de misiones interactivo.
Tus decisiones determinarán el destino de tus amigos.
¡Ten cuidado y buena suerte!

CONTEXTO:
Un paseo por el bosque terminó en pesadilla. Tus amigos han sido
arrastrados al interior de una construcción de madera podrida.
Estás solo, con un manojo de llaves oxidadas y una navaja.

Frente a ti, la puerta principal emite un hedor a moho y algo metálico.
Sientes que la madera pulsa como si tuviera un corazón propio.

¿Qué decides hacer?
1 - Arremeter contra la madera con el hombro
2 - Probar las llaves oxidadas en la cerradura
3 - Forzar la cerradura con la navaja
4 - Bordear la estructura buscando otra entrada''')

ans1 = input("> ")

if ans1 == "1":
    print('''
[RESULTADO]: La puerta es de roble reforzado. Solo logras un fuerte dolor
en el hombro y escuchas un gruñido desde el interior. Debes buscar otro camino.''')
elif ans1 == "2":
    print('''
[RESULTADO]: Las llaves no encajan en absoluto. El mecanismo parece
sellado por una fuerza invisible o una sustancia extraña.''')
elif ans1 == "3":
    print('''
[RESULTADO]: La hoja de tu navaja se dobla peligrosamente. La cerradura
está llena de una sustancia pegajosa negra que desprende calor.''')
else:
    print('''
[RESULTADO]: Decides ser cauteloso. Al bordear la cabaña, evitas la trampa
de la entrada principal y encuentras una debilidad en el lateral.''')

# --- ACTO 2: LA VENTANA DEL PÁNICO ---
print('''
----------------------------------------------------
Llegas a una ventana trasera. El vidrio está sucio, pero ves sombras
moviéndose dentro. El pestillo interior está a la vista por una grieta.

¿Cómo entrarás?
1 - Maniobrar el pestillo con la punta de la navaja
2 - Romper el cristal de un golpe con una piedra
3 - Intentar desmantelar el marco de madera podrida
4 - Gritar para localizar a tus amigos primero''')

ans2 = input("> ")

if ans2 == "1":
    print('''
[ÉXITO]: Con precisión quirúrgica, deslizas el seguro.
La ventana cede sin hacer ruido. Logras cruzar la casa en silencio.''')
elif ans2 == "2":
    print('''
[RIESGO]: El estruendo es ensordecedor. Escuchas gritos inhumanos
acercándose. Tienes que correr frenéticamente hacia el patio trasero.''')
elif ans2 == "3":
    print('''
[RETRASO]: Pierdes demasiado tiempo luchando con los clavos oxidados.
Sientes que la oscuridad de la casa te observa. Llegas tarde al patio.''')
else:
    print('''
[FALLO]: Tu grito atrae a una presencia oscura del bosque.
Debes huir despavorido hacia la zona trasera para no ser capturado.''')

# --- ACTO 3: EL ALTAR DE LAS SOMBRAS ---
print('''
----------------------------------------------------
Logras llegar al patio trasero. Allí ves una jaula de hierro viejo
colgando sobre un foso oscuro. Tus amigos están dentro, aterrados.
Una cerradura rúnica brilla con una luz mortecina en la base.

En el suelo, encuentras una llave que emite un tenue brillo azul.

¡Es el momento final! ¿Qué haces?
1 - Intentar cortar los barrotes con la navaja
2 - Sacudir la estructura para acercarla a tierra firme
3 - Usar la llave brillante que encontraste en el altar
4 - Patear el mecanismo de anclaje de la cadena''')

ans3 = input("> ")

if ans3 == "3":
    print('''
****************************************************
¡VICTORIA! La llave encaja perfectamente con la runa.
La cerradura se deshace como ceniza y la jaula se abre.
Tus amigos están libres y la maldición del bosque se desvanece.
****************************************************''')
elif ans3 == "2":
    print('''
[TRAGEDIA]: El soporte podrido no aguanta el peso extra.
La jaula cede y cae al foso profundo. Has fallado la misión.''')
elif ans3 == "1":
    print('''
[FALLO]: El acero es mágico. Tu navaja se rompe en pedazos.
No tienes forma de abrir la jaula. El tiempo se agota...''')
else:
    print('''
[DESASTRE]: El impacto bloquea el engranaje permanentemente.
La jaula queda suspendida para siempre. Te quedas solo en el bosque.''')

print("\nFin del juego. Gracias por jugar.")
