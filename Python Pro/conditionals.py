# Ejemplo 1: Decidir qué ropa usar según el clima
clima = input("¿Cómo está el clima hoy? (soleado, lluvioso, frío): ")

if clima == "soleado":
    print("Usar camiseta y pantalones cortos.")
elif clima == "lluvioso":
    print("Llevar un paraguas y una chaqueta.")
elif clima == "frío":
    print("Usar un suéter y pantalones largos.")
else:
    print("No comprendo el clima.")

# Ejemplo 2: Planificar una salida según el tiempo libre y el clima
tiempo_libre = input("¿Tienes tiempo libre ahora? (sí, no): ")
clima = input("¿Cómo está el clima? (soleado, lluvioso, frío): ")

if tiempo_libre == "sí":
    if clima == "soleado":
        print("Ir al parque a jugar al fútbol.")
    elif clima == "lluvioso":
        print("Quedarse en casa y ver una película.")
    elif clima == "frío":
        print("Ir al cine o visitar a un amigo.")
    else:
        print("No comprendo el clima.")
else:
    print("Volver a la tarea o a otras actividades.")

# Ejemplo 3: Tomar decisiones sobre el tiempo de estudio
examen_manana = input("¿Tienes un examen mañana? (sí, no): ")

if examen_manana == "sí":
    print("Estudiar más y jugar menos.")
else:
    print("Estudiar según lo planeado y luego tomar un descanso.")

# Ejemplo 4: Decidir qué comer según el hambre y los alimentos disponibles
hambre = input("¿Tienes hambre? (sí, no): ")

if hambre == "sí":
    print("Preparar un sándwich o calentar una pizza.")
else:
    print("Tomar una fruta o un yogur.")

# Ejemplo 5: Planificar las tareas del hogar
dia_semana = input("¿Qué día de la semana es hoy? (lunes, martes, ..., domingo): ")

if dia_semana == "sábado" or dia_semana == "sábado":
    print("Ayudar a tus padres con la limpieza.")
else:
    print("Continuar con la tarea o hacer otras actividades.")
