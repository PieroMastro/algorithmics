# ==============================================================================
# SISTEMA DE ALMACENAMIENTO DE EMPLEADOS - PROTEAM
# ==============================================================================

# Lista principal donde se almacenarán los diccionarios de cada empleado
empleados = []

# ------------------------------------------------------------------------------
# 1. REGISTRO DE DATOS
# ------------------------------------------------------------------------------
# TODO: Crear 3 diccionarios con los datos de 3 empleados.
# Cada diccionario debe tener las siguientes claves:
#   - "apellido" (string)
#   - "puesto" (string)
#   - "eficacia" (float o int)
#   - "proyectos" (lista con 3 strings)

# Ejemplo de estructura de un empleado (puedes borrarlo o usarlo de guía):
# empleado1 = {
#     "apellido": "García",
#     "puesto": "Desarrollador",
#     "eficacia": 8.5,
#     "proyectos": ["Sistema Web", "App Móvil", "Migración DB"]
# }

# TODO: Define aquí los 3 empleados:
# empleado1 = {...}
# empleado2 = {...}
# empleado3 = {...}

# TODO: Agrega los 3 empleados a la lista 'empleados' usando .append()
# empleados.append(empleado1)
# ...


# ------------------------------------------------------------------------------
# 2. FUNCIONES DE CONSULTA
# ------------------------------------------------------------------------------

def mostrar_apellidos(lista_empleados):
    """Recorre la lista e imprime el apellido de todos los empleados."""
    print("--- Apellidos de todos los empleados ---")
    # TODO: Usar un bucle 'for' para recorrer 'lista_empleados'
    # Acceder a la clave "apellido" de cada diccionario e imprimirla
    pass


def mostrar_empleado_mas_eficaz(lista_empleados):
    """Busca e imprime el apellido del empleado con mayor coeficiente de eficacia."""
    print("\n--- Empleado más eficaz ---")
    # TODO: Lógica para encontrar el empleado con mayor eficacia.
    # Pista: Puedes usar un bucle 'for' para comparar la eficacia de cada uno
    # o usar la función nativa max().
    pass


def mostrar_puestos(lista_empleados):
    """Recorre la lista e imprime los puestos de todos los empleados."""
    print("\n--- Puestos de todos los empleados ---")
    # TODO: Usar un bucle 'for' para recorrer 'lista_empleados'
    # Acceder a la clave "puesto" de cada diccionario e imprimirla
    pass


# ------------------------------------------------------------------------------
# 3. EJECUCIÓN (EN UN MÓDULO APARTE)
# ------------------------------------------------------------------------------
# TODO: Descomenta estas líneas para probar tus funciones una vez programadas:

# mostrar_apellidos(empleados)
# mostrar_empleado_mas_eficaz(empleados)
# mostrar_puestos(empleados)
