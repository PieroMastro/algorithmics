# ==============================================================================
# MÓDULO PRINCIPAL - INTERFAZ DE USUARIO Y CICLO DEL SISTEMA
# ==============================================================================

# Importamos la lista de empleados y las funciones del otro archivo/módulo
from proteam_logic import (
    empleados,
    obtener_apellidos,
    obtener_empleado_mas_eficaz,
    obtener_puestos
)

def mostrar_menu():
    """Muestra las opciones disponibles en pantalla."""
    print("\n" + "="*40)
    print("    SISTEMA DE GESTIÓN PROTEAM")
    print("="*40)
    print("1. Ver apellidos de todos los empleados")
    print("2. Ver apellido del empleado más eficaz")
    print("3. Ver puestos de todos los empleados")
    print("0. Salir del sistema")
    print("-" * 40)


def iniciar_sistema():
    """Ciclo principal que maneja las solicitudes del usuario."""
    ejecutando = True
    
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-3): ").strip()



# Punto de arranque del programa
if __name__ == "__main__":
    iniciar_sistema()
