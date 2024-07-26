saludo = input("Ingrese su nombre: ")

print("Hola", saludo)

pregunta = input("¿Cómo estas?: ")

if pregunta.lower() == 'bien':
    print("Que bueno. Comencemos!")
elif pregunta.lower() == 'mal':
    print("Que lamentable. Espero que luego de utilizar mi app te sientas mejor!")
else:
    print("Ok.")


question = int(input('''¿Que quieres hacer?,

Ingresa 1, 2, 3, 4, 5 o 6:

    1) Sacar valor absoluto, error absoluto, desviación media, y rango.
    2) Obtener un elemento de física.
    3) Encontrar elemento de la tabla periódica.
    4) Transformar unidades al sistema M.K.S.
    5) Genética.
    6) Tabla de productos.
'''))


print("")


def physics_calculations_valores():

    print("-----------------------------------------------------------")
    valor1 = float(input("Ingrese su primer valor: "))
    valor2 = float(input("Ingrese su segundo valor:"))
    valor3 = float(input("Ingrese su tercer valor: "))
    valor4 = float(input("Ingrese su cuarto valor: "))
    valor5 = float(input("Ingrese su quinto valor: "))
    print("-----------------------------------------------------------")
    print("El valor promedio de tu lista de valores, es: ", (valor1 + valor2 + valor3 + valor4 + valor5)/ 5)
    Vp = ((valor1 + valor2 + valor3 + valor4 + valor5)/ 5)
    print("-----------------------------------------------------------")
    print("A: ", (valor1 - Vp))

    Ea = (valor1 - Vp)
    my_float1 = Ea

    result10 = round(my_float1, 2)

    print("B: ", (valor2 - Vp))

    Ea1 = (valor2 - Vp)
    my_float2 = Ea1

    result11 = round(my_float2, 2)

    print("C: ", (valor3 - Vp))

    Ea2 = (valor3 - Vp)
    my_float3 = Ea2

    result12 = round(my_float3, 2)

    print("D: ", (valor4 - Vp))

    Ea3 = (valor4 - Vp)
    my_float4 = Ea3

    result13 = round(my_float4, 2)

    print("E: ", (valor5 - Vp))


    Ea4 = (valor5 - Vp)
    my_float5 = Ea4

    result14 = round(my_float5, 2)

    print("-----------------------------------------------------------")

    number = result10
    result = abs(number)
    print("El 1er error absoluto es: ", result)



    number2 = result11
    result2 = abs(number2)
    print("El 2do error absoluto es: ", result2)


    number3 = result12
    result3 = abs(number3)
    print("El 3er error absoluto es: ", result3)



    number4 = result13
    result4 = abs(number4)
    print("El 4to error absoluto es: ", result4)



    number5 = result14
    result5 = abs(number5)
    print("El 5to error absoluto es: ", result5)

    print("-----------------------------------------------------------")

    print("La desviación media de los valores, es: ", (result + result2 + result3 + result4 + result5)/ 5)
    Dm = ((result + result2 + result3 + result4 + result5)/ 5)
    print("-----------------------------------------------------------")
    a = (Vp + Dm)
    b = (Vp - Dm)

    number6 = (Vp - Dm)
    result6 = abs(number6)
    (result6)
    print("-----------------------------------------------------------")
    print("Entre este valor: ", (Dm + Vp))
    print("Y este otro valor: ", (number6))
    print("-----------------------------------------------------------")

    if valor1 <= a and valor1 >= number6:
        print("Sí está en el rango = ", valor1)
    else:
        print("No está en el rango = ", valor1)

    if valor2 <= a and valor2 >= number6:
        print("Sí está en el rango = ", valor2)
    else:
        print("No está en el rango = ", valor2)
        
    if valor3 <= a and valor3 >= number6:
        print("Sí está en el rango = ", valor3)
    else:
        print("No está en el rango = ", valor3)
            
    if valor4 <= a and valor4 >= number6:
        print("Sí está en el rango = ", valor4)
    else:
        print("No está en el rango = ", valor4)
                
    if valor5 <= a and valor5 >= number6:
        print("Sí está en el rango = ", valor5)
    else:
        print("No está en el rango = ", valor5)



def physics_calculations():


    print("-----------------------------------------------------------")
    print("¿Qué quieres conseguir?")
    print("""
    1- Velocidad media
    2- Rapidez media
    3- Rapidez Inicial
    4- Rapidez Final
    5- Peso
    6- Desplazamiento
    7- Desplazamiento en función del tiempo
    8- Fuerza Aplicada""")
    print("-----------------------------------------------------------") 
    OP = float(input("Seleccione: 1,  2,  3,  4,  5,  6,  7  u  8"))
    print("-----------------------------------------------------------")


    if OP == 1:

        OP1 = float(input("Escriba la posición inicial del cuerpo (Sin unidades)"))
        OP2 = float(input("Escriba la posición final del cuerpo (Sin unidades)"))
        OP3 = float(input("Escriba el tiempo inicial del cuerpo (Sin unidades)"))
        OP4 = float(input("Escriba el tiempo final del cuerpo (Sin unidades)"))
        print("-----------------------------------------------------------")
        R = (OP2 - OP1)
        R1 = (OP4 - OP3)
        Respuesta = R / R1
        T114 = round(Respuesta, 2)
        print("La velocidad media del cuerpo es de: ", T114, "m/s i")
        print("-----------------------------------------------------------")
    


    elif OP == 2:
        OP5 = float(input("Escriba la posición final del cuerpo (Sin unidades)")) 
        OP6 = float(input("Escriba el tiempo final del cuerpo (Sin unidades)"))
        print("-----------------------------------------------------------")
        Respuesta1 = OP5 / OP6
        T113 = round(Respuesta1, 2)
        print("La rapidez media del cuerpo es de: ", T113, "m/s")
        print("-----------------------------------------------------------")

    

    elif OP == 3:
        OP5 = float(input("Escriba la rapidez inicial del cuerpo (Sin unidades)")) 
        OP6 = float(input("Escriba el tiempo final del cuerpo (Sin unidades)"))
        OP7 = float(input("Escriba la aceleración del cuerpo (Sin unidades)"))
        R3 = OP7 * OP6
        R4 = OP5 + R3
        T112 = round(R4, 2)
        print("-----------------------------------------------------------")
        print("La rapidez final del cuerpo es de: ", T112, "m/s")
        print("-----------------------------------------------------------")
        



    elif OP == 4:
        OP8 = float(input("Escriba la rapidez final del cuerpo (Sin unidades)")) 
        OP9 = float(input("Escriba el tiempo final del cuerpo (Sin unidades)"))
        OP10 = float(input("Escriba la aceleración del cuerpo (Sin unidades)"))
        print("-----------------------------------------------------------")
        R99 = OP10 * OP9
        Respuesta4 = OP8 / R99
        T111 = round(Respuesta4, 2)
        print("La rapidez inicial del cuerpo es de: ", T111, "m/s")
        print("-----------------------------------------------------------")

   
    

    elif OP == 5:
        OP11 = float(input("Escriba la masa del cuerpo (Sin unidades)")) 
        OP12 = float(input("Escriba en que planeta se esta llevando a cabo el movimiento/ 1) Mercurio, 2) Venus, 3) Tierra, 4) Marte, 5) Júpiter, 6) Saturno, 7) Urano y 8) Neptuno"))
        print("-----------------------------------------------------------")
        if OP12 == 1:
            Respuesta5 = OP11 * 3.7
            T110 = round(Respuesta5, 2)
            print("El peso del cuerpo en Mercurio es de: ", T110, "N")
        if OP12 == 2:
            Respuest = OP11 * 8.87
            T109 = round(Respuest, 2)
            print("El peso del cuerpo en Venus es de: ", T109, "N")
        if OP12 == 3:
            Respues = OP11 * 9.8
            T108 = round(Respues, 2)
            print("El peso del cuerpo en la Tierra es de: ", T108, "N")
        if OP12 == 4:
            Respue = OP11 * 3.71
            T107 = round(Respue, 2)
            print("El peso del cuerpo en Marte es de: ", T107, "N")
        if OP12 == 5:
            Respu = OP11 * 24.79
            T106 = round(Respu, 2)
            print("El peso del cuerpo en Júpiter es de: ", T106, "N")
        if OP12 == 6:
            Resp = OP11 * 10.44
            T105 = round(Resp, 2)
            print("El peso del cuerpo en Saturno es de: ", T105, "N")
        if OP12 == 7:
            Res = OP11 * 8.87
            T104 = round(Res, 2)
            print("El peso del cuerpo en Urano es de: ", T104, "N")
        if OP12 == 8:
            Re = OP11 * 11.15
            T103 = round(Re, 2)
            print("El peso del cuerpo en Neptuno es de: ", T103, "N")
        print("-----------------------------------------------------------")

    elif OP == 6:
        OP13 = float(input("Escriba la posición inicial del cuerpo (Sin unidades)"))
        OP14 = float(input("Escriba la posición final del cuerpo (Sin unidades)"))
        Re6 = OP14 - OP13
        T102 = round(Re6, 2)
        print("-----------------------------------------------------------")
        print("El cuerpo se desplazó: ", T102, "m")
        print("-----------------------------------------------------------")

    elif OP == 7:        
        OP15 = float(input("Escriba la rapidez inicial del cuerpo (Sin unidades)")) 
        OP16 = float(input("Escriba el tiempo final del cuerpo (Sin unidades)"))
        OP17 = float(input("Escriba la aceleración del cuerpo (Sin unidades)"))
        print("-----------------------------------------------------------")
        Re8 = OP16 * OP16
        Re9 = OP15 * OP16
        Re10 = Re8 * OP17
        Re11 = Re10 / 2
        Re12 = Re9 + Re11
        T101 = round(Re12, 2)
        print("El cuerpo se desplazó: ", Re12, "m, en",T101, "s")
        print("-----------------------------------------------------------")


    elif OP == 8:
        OP18 = float(input("Escriba la masa del cuerpo (Sin unidades)"))
        OP19 = float(input("Escriba la aceleración del cuerpo (Sin unidades)"))
        Re13 = OP18 * OP19
        T100 = round(Re13, 2)

        print("-----------------------------------------------------------")
        print("El cuerpo de", OP18, "Kg, para ser movido con una aceleración de", OP19, "m/s2, se necesita aplicar una fuerza de", T100, "N")
        print("-----------------------------------------------------------")

 
def periodic_table():


    print("¿Qué elemento de la tabla periódica quieres encontrar?")
    print("-----------------------------------------------------------")
    tabla = input("H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn, Fr, Ra, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Nh, Fl, Mc, Lv, Ts, Og")
    print("-----------------------------------------------------------")

    if tabla in ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']:
        print("Grupo 1 /", tabla, "/")
    elif tabla in ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']:
        print("Grupo 2 /", tabla, "/")
    elif tabla in ['Sc', 'Y', 'La', 'Ac']:
        print("Grupo 3 /", tabla, "/")
    elif tabla in ['Ti', 'Zr', 'Hf', 'Rf']:
        print("Grupo 4 /", tabla, "/")
    elif tabla in ['V', 'Nb', 'Ta', 'Db']:
        print("Grupo 5 /", tabla, "/")
    elif tabla in ['Cr', 'Mo', 'W', 'Sg']:
        print("Grupo 6 /", tabla, "/")
    elif tabla in ['Mn', 'Tc', 'Re', 'Bh']:
        print("Grupo 7 /", tabla, "/")
    elif tabla in ['Fe', 'Ru', 'Os', 'Hs']:
        print("Grupo 8 /", tabla, "/")
    elif tabla in ['Co', 'Rh', 'Ir', 'Mt']:
        print("Grupo 9 /", tabla, "/")
    elif tabla in ['Ni', 'Pd', 'Pt', 'Ds']:
        print("Grupo 10 /", tabla, "/")
    elif tabla in ['Cu', 'Ag', 'Au', 'Rg']:
        print("Grupo 11 /", tabla, "/")
    elif tabla in ['Zn', 'Cd', 'Hg', 'Cn']:
        print("Grupo 12 /", tabla, "/")
    elif tabla in ['B', 'Al', 'Ga', 'In', 'Tl', 'Nh']:
        print("Grupo 13 /", tabla, "/")
    elif tabla in ['C', 'Si', 'Ge', 'Sn', 'Pb', 'Fl']:
        print("Grupo 14 /", tabla, "/")
    elif tabla in ['N', 'P', 'As', 'Sb', 'Bi', 'Mc']:
        print("Grupo 15 /", tabla, "/")
    elif tabla in ['O', 'S', 'Se', 'Te', 'Po', 'Lv']:
        print("Grupo 16 /", tabla, "/")
    elif tabla in ['F', 'Cl', 'Br', 'I', 'At', 'Ts']:
        print("Grupo 17 /", tabla, "/")
    elif tabla in ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Og']:
        print("Grupo 18 /", tabla, "/")
    
    
    
    if tabla in ['H', 'He']:
        print("Período 1 /", tabla, "/")
    elif tabla in ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']:
        print("Período 2 /", tabla, "/")
    elif tabla in ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']:
        print("Período 3 /", tabla, "/")
    elif tabla in ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']:
        print("Período 4 /", tabla, "/")
    elif tabla in ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe']:
        print("Período 5 /", tabla, "/")
    elif tabla in ['Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']:
        print("Período 6 /", tabla, "/")
    elif tabla in ['Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']:
        print("Período 7 /", tabla, "/")

           


def unit_conversion():



    print("-----------------------------------------------------------")
    print("¿En que unidad está tú valor?")
    print("-----------------------------------------------------------")
    transformar1 = input("Hora (t), Minuto (t), Km (l), cm (l), Pulgada (l), Gramo (m), Tonelada (m), Libra (m)")
    print("-----------------------------------------------------------")
    Transforma = float(input("Escriba su valor (Sin unidades)"))
    print("-----------------------------------------------------------")
    
    if transformar1 == "Hora":
        T1 = Transforma * 3600
        T11 = round(T1, 2)
        print(Transforma, "h, en s, sería", T11, "s")
    elif transformar1 == "Minuto":
        T2 = Transforma * 60
        T21 = round(T2, 2)
        print(Transforma, "min, en s, sería", T21, "s")
    elif transformar1 == "Km":
        T3 = Transforma * 1000
        T31 = round(T3, 2)
        print(Transforma, "Km, en m, sería", T31, "m")
    elif transformar1 == "cm":
        T4 = Transforma / 100
        print(Transforma, "cm, en m, sería", T4, "m")
    elif transformar1 == "Pulgada":
        T5 = Transforma * 0.0254
        T51 = round(T5, 2)
        print(Transforma, "in, en m, sería", T51, "m")
    elif transformar1 == "Gramo":
        T6 = Transforma / 1000
        print(Transforma, "g, en Kg, sería", T6, "Kg")
    elif transformar1 == "Tonelada":
        T7 = Transforma * 1000
        T71 = round(T7, 2)
        print(Transforma, "t, en Kg, sería", T71, "Kg")
    elif transformar1 == "Libra":
        T8 = Transforma * 0.454
        T81 = round(T8, 2)
        print(Transforma, "lb, en Kg, sería", T81, "Kg")





def genetics():


    print("-----------------------------------------------------------")
    A = input("caracteristica dominante")
    print("-----------------------------------------------------------")
    a = input("caracteristica reseciva")
    print("-----------------------------------------------------------")
    padre = input("escribe los alelos del padre (Siempre el dominante primero, ejemplo: Aa)")
    print("-----------------------------------------------------------")
    madre = input("escribe los alelos de la madre (Siempre el dominante primero, ejemplo: aa)")

    if len(padre) > 1:
        primeraletra = padre[1]

    if len(padre) > 0:
        primeraletra1 = padre[0]



    if len(madre) > 1:
        primeraletra2 = madre[1]

    if len(madre) > 0:
        primeraletra3 = madre[0]

    
    gen1 = primeraletra1 + primeraletra3
    gen2 = primeraletra1 + primeraletra2

    print("-----------------------------------------------------------")
    print(gen1, "____", gen2)


    gen3 = primeraletra + primeraletra3
    gen4 = primeraletra + primeraletra2

    letra0 = "a"
    letra1 = "A"
        

    print(gen3, "____", gen4)
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")

   
    count_A = 0
    count_a = 0

    genotipos = [gen1, gen2, gen3, gen4]
    for gen in genotipos:
        if gen[0] == "A":
            count_A += 1
    for gen in genotipos:
        
        if gen[0] == "a":
            count_a += 1
            

    total_genes = count_A + count_a
    if total_genes > 0:
        porcentaje_A = (count_A / total_genes) * 100
        porcentaje_a = (count_a / total_genes) * 100
    else:
        porcentaje_A = 0
        porcentaje_a = 0

    print(porcentaje_A, A, "y", porcentaje_a, a)


   


def product_inventory():


    print("-----------------------------------------------------------")

    entrada = input("ingrese 10 productos diferentes separados por comas y sin espacio entre ellos, ejemplo: a,b,c... ")
    palabras = entrada.split(',')
    print("-----------------------------------------------------------")


    if palabras:
        palabra0 = palabras[0]
        print("1)", palabra0)
        cantidad0 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra1 = palabras[1]
        print("2)", palabra1)
        cantidad1 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")
    
    if palabras:
        palabra2 = palabras[2]
        print("3)", palabra2)
        cantidad2 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra3 = palabras[3]
        print("4)", palabra3)
        cantidad3 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra4 = palabras[4]
        print("5)", palabra4)
        cantidad4 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra5 = palabras[5]
        print("6)", palabra5)
        cantidad5 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra6 = palabras[6]
        print("7)", palabra6)
        cantidad6 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra7 = palabras[7]
        print("8)", palabra7)
        cantidad7 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra8 = palabras[8]
        print("9)", palabra8)
        cantidad8 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")

    if palabras:
        palabra9 = palabras[9]
        print("10)", palabra9)
        cantidad9 = int(input("Cantidad:"))
        print("-----------------------------------------------------------")
        print("__________________________________________________________")


    print("REPORTE FINAL")
    print(palabra0, "------", cantidad0)
    print(palabra1, "------", cantidad1)
    print(palabra2, "------", cantidad2)
    print(palabra3, "----------", cantidad3)
    print(palabra4, "--------", cantidad4)
    print(palabra5, "---------", cantidad5)
    print(palabra6, "---------", cantidad6)
    print(palabra7, "--------", cantidad7)
    print(palabra8, "-------", cantidad8)
    print(palabra9, "-------", cantidad9)

    print("__________________________________________________________")
    print("-----------------------------------------------------------")




def geometria():

    print(" (1) Sacar la suma de los angulos de una figura geométrica")
    print(" (2) Obtener el volumen de una figura geométrica")
    print("-----------------------------------------------------------")
    geom3 = input("(1) o (2)")
    print("-----------------------------------------------------------")

    if geom3 == "1":
        geom = input("¿Qué figura quieres analizar / Triángulo, Cuadrado, Rectángulo, Pentágono, Hexágono, Heptágono, Octágono, Eneágono, Decágono, otra")


        if geom == "Triángulo":
            tri = 3 - 2
            tri1 = tri * 180
            print("La suma de todos los ángulos del", geom, "es igual a", tri1)
        if geom == "Cuadrado":
            cua = 4 - 2
            cua1 = cua * 180
            print("La suma de todos los ángulos del", geom, "es igual a", cua1)
        if geom == "Rectángulo":
            rec = 4 - 2
            rec1 = rec * 180
            print("La suma de todos los ángulos del", geom, "es igual a", rec1)
        if geom == "Pentágono":
            pen = 5 - 2
            pen1 = pen * 180
            print("La suma de todos los ángulos del", geom, "es igual a", pen1)
        if geom == "Hexágono":
            Hex = 6 - 2 
            Hex1 = Hex * 180
            print("La suma de todos los ángulos del", geom, "es igual a", Hex1)
        if geom == "Heptágono":
            Hep = 7 - 2
            Hep1 = Hep * 180
            print("La suma de todos los ángulos del", geom, "es igual a", Hep1)
        if geom == "Octágono":
            Oct = 8 - 2
            Oct1 = Oct * 180
            print("La suma de todos los ángulos del", geom, "es igual a", Oct1)
        if geom == "Eneágono":
            Ene = 9 - 2
            Ene1 = Ene * 180
            print("La suma de todos los ángulos del", geom, "es igual a", Ene1)
        if geom == "Decágono":
            Dec = 10 - 2
            Dec1 = Dec * 180
            print("La suma de todos los ángulos del", geom, "es igual a", Dec1)
        if geom == "otra":
            geo8 = input("¿Cuántos lados tiene la figura que quieres analizar?")
            otr = geo8 - 2
            otr1 = otr * 180
            print("La suma de todos los ángulos del", geom, "es igual a", otr1)

        



    if geom3 == "2":
        geom1 = input("Obtener el volumen de un: circulo, cuadrado, rectangulo, triangulo o cilindro")


        if geom1 == "circulo":             
            geom2 = int(input("Escribe el radio del circulo"))           
            a = 1.33 * 3.14             
            b = geom2 * geom2
            c = i * geom2             
            d = c * r
            geom4 = round(d, 2)            
            print(geom4, "unidades cúbicas")


        if geom1 == "cuadrado":                      
            geom6 = int(input("Escribe la longitud de uno de los lados del cuadrado"))            
            e = geom6 * geom6
            f = e * geom6            
            geom5 = round(f, 2)            
            print(geom5, "unidades cúbicas")


        if geom1 == "rectangulo":             
            geo = int(input("escribe el alto del rectangulo"))            
            geo1 = int(input("escribe el ancho del rectangulo"))
            geo2 = int(input("escribe el largo del rectangulo"))
            h = geo * geo1
            i = h * geo2
            geom7 = round(i, 2)            
            print(geom7, "unidades cúbicas")


        if geom1 == "triangulo":
            geo3 = int(input("escribe el alto del triangulo"))            
            geo4 = int(input("Escribe el radio del triangulo"))           
            j = geo3 * 3.14             
            k = geo4 * geo4
            l = j * k           
            m = l / 3
            geom8 = round(m, 2)            
            print(geom8, "unidades cúbicas")


        if geom1 == "cilindro":
            geo5 = int(input("escribe el alto del cilindro"))            
            geo6 = int(input("Escribe el radio del cilindro"))           
            n = geo5 * 3.14             
            o = geo6 * geo6
            p = n * o          
            geom9 = round(o, 2)            
            print(geom9, "unidades cúbicas")
        






if question == 1:
    physics_calculations_valores()
elif question == 2:
    physics_calculations()
elif question == 3:
    periodic_table()
elif question == 4:
    unit_conversion()
elif question == 5:
    genetics()
elif question == 6:
    product_inventory()
elif question == 7:
    geometria()
    
