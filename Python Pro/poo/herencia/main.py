# ==========================================
# CLASE BASE
# ==========================================
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def obtener_info(self) -> str:
        # TODO: Retornar string con el formato "Producto: [nombre] | Precio: $[precio] | Stock: [cantidad]"
        pass

    def calcular_total(self) -> float:
        # TODO: Retornar el valor total del producto (precio * cantidad)
        pass


# ==========================================
# CLASE DERIVADA (HERENCIA)
# ==========================================
class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, dias_para_vencer: int):
        # TODO: Invocar al constructor de la clase madre usando super()
        # TODO: Asignar el atributo propio 'dias_para_vencer'
        pass

    def obtener_info(self) -> str:
        # TODO: Reutilizar el método obtener_info() del padre y agregar "| Vence en: X días"
        pass


# ==========================================
# CLASE GESTORA E INTERFAZ CLI
# ==========================================
class GestorInventario:
    def __init__(self):
        # TODO: Inicializar la lista vacía self.productos
        pass

    def agregar_producto(self, producto: Producto):
        # TODO: Añadir el objeto 'producto' a la lista self.productos
        # TODO: Mostrar mensaje de confirmación en consola
        pass

    def mostrar_inventario(self):
        # TODO: Verificar si la lista está vacía y notificar al usuario
        # TODO: Recorrer self.productos, imprimir p.obtener_info() y sumar el total de p.calcular_total()
        # TODO: Mostrar el valor total acumulado del inventario
        pass

    def menu(self):
        while True:
            print("=== GESTOR DE INVENTARIO (POO) ===")
            print("1. Agregar Producto General")
            print("2. Agregar Producto Perecedero")
            print("3. Mostrar Inventario")
            print("4. Salir")
            opcion = input("Selecciona una opción (1-4): ")

            if opcion == "1":
                nom = input("Nombre: ")
                pre = float(input("Precio: "))
                cant = int(input("Cantidad: "))
                prod = Producto(nom, pre, cant)
                self.agregar_producto(prod)

            elif opcion == "2":
                nom = input("Nombre: ")
                pre = float(input("Precio: "))
                cant = int(input("Cantidad: "))
                dias = int(input("Días para vencer: "))
                # TODO: Crear la instancia de ProductoPerecedero y agregarla con self.agregar_producto()
                pass

            elif opcion == "3":
                self.mostrar_inventario()

            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.\n")


# Punto de entrada
if __name__ == "__main__":
    app = GestorInventario()
    app.menu()
