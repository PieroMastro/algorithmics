# ==============================================================================
# MÓDULO DE LÓGICA Y DATOS DE PROTEAM
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BASE DE DATOS (Lista de diccionarios)
# ------------------------------------------------------------------------------
# TODO: Crea los diccionarios con los datos de 3 empleados.
# Estructura requerida para cada diccionario:
#   - "apellido": string
#   - "puesto": string
#   - "eficacia": float o int
#   - "proyectos": lista de 3 strings

empleado1 = {
    # TODO: Completa los datos del empleado 1
}

empleado2 = {
    # TODO: Completa los datos del empleado 2
}

empleado3 = {
    # TODO: Completa los datos del empleado 3
}

# Lista principal con todos los empleados
# TODO: Asegúrate de agregar los 3 diccionarios a esta lista
empleados = [empleado1, empleado2, empleado3]


# ------------------------------------------------------------------------------
# 2. FUNCIONES DE CONSULTA
# ------------------------------------------------------------------------------

def obtener_apellidos(lista_empleados):
    """Devuelve o imprime la lista con los apellidos de todos los empleados."""
    print("\n--- APELLIDOS DE TODOS LOS EMPLEADOS ---")
    # TODO: Recorrer 'lista_empleados' con un bucle 'for' e imprimir cada apellido
    pass


def obtener_empleado_mas_eficaz(lista_empleados):
    """Devuelve o imprime el apellido del empleado con mayor coeficiente de eficacia."""
    print("\n--- EMPLEADO MÁS EFICAZ ---")
    # TODO: Programar la lógica para determinar cuál empleado tiene la mayor eficacia
    # e imprimir su apellido.
    pass


def obtener_puestos(lista_empleados):
    """Devuelve o imprime los puestos de todos los empleados."""
    print("\n--- PUESTOS DE TODOS LOS EMPLEADOS ---")
    # TODO: Recorrer 'lista_empleados' con un bucle 'for' e imprimir cada puesto
    pass

# ------------------------------------------------------------------------------
# 3. EJECUCIÓN (EN UN MÓDULO APARTE)
# ------------------------------------------------------------------------------
# TODO: Descomenta estas líneas para probar tus funciones una vez programadas:

# mostrar_apellidos(empleados)
# mostrar_empleado_mas_eficaz(empleados)
# mostrar_puestos(empleados)
