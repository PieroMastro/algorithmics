# ==========================================
# COMPONENTES DEL MENÚ (CLASES BASE)
# ==========================================
class Dish():
    def __init__(self, dish_id: int, name: str, description: str, price: float):
        self.dish_id = dish_id
        self.name = name
        self.description = description
        self.price = price

    def get_dish_info(self):
        return f'{self.name}: {self.description} - ${self.price}'


class Menu():
    def __init__(self, name: str):
        self.name = name
        self.products = list()

    def set_menu(self, item: Dish):
        self.products.append(item)

    def get_menu(self):
        print(f'\n- {self.name} -')
        for item in self.products:
            print(item.get_dish_info())
        return self.products


# ==========================================
# CLASE ENTRANTE / GESTORA (EJERCICIO TODO)
# ==========================================
class Order():
    def __init__(self, number: int):
        # TODO: Asignar el número de mesa recibido por parámetro al atributo 'number'
        # TODO: Inicializar una lista vacía para almacenar los platillos ('order')
        # TODO: Inicializar el acumulador de precio total en 0 ('total')
        pass

    def set_order(self, item: Dish):
        # TODO: Añadir el objeto 'item' (platillo) a la lista de la orden
        # TODO: Sumar el precio del platillo al acumulador del total
        pass

    def get_order(self) -> list:
        # TODO: Retornar la lista que contiene todos los platillos pedidos
        pass

    def get_total(self) -> float:
        # TODO: Retornar el valor final acumulado en el total
        pass


# ==========================================
# LÓGICA DE NEGOCIO Y CONTROLADORES
# ==========================================
def menu_entry(menu: Menu):
    """Solicita platillos al usuario para llenar el menú del restaurante."""
    num = int(input("¿Cuántos platillos desea agregar al menú? "))
    for i in range(num):
        dish_id = i + 1
        name = input("Ingrese el platillo: ")
        description = input("Ingrese la descripción del platillo: ")
        price = float(input("Ingrese el precio de 1 porción: "))
        
        dish = Dish(dish_id, name, description, price)
        menu.set_menu(dish)


def order_entry(menu: Menu):
    """Gestiona la toma de un pedido vinculando platos del menú con una Orden."""
    mesa = int(input("Número de mesa: "))
    
    # Instanciación de la clase Order administrada por el estudiante
    order = Order(mesa)
    
    num = int(input("¿Cuántos platillos desea pedir? "))
    for i in range(num):
        question = input('Ingrese el nombre del platillo: ')
        found = False
        
        # Búsqueda del platillo en el inventario del menú
        for item in menu.products:
            if item.name.lower() == question.lower():
                # TODO: Descomentar la siguiente línea una vez implementado 'set_order' en la clase Order
                # order.set_order(item)
                found = True
                break
                
        if not found:
            print(f'El platillo "{question}" no está en el menú.')
            
    # Visualización del ticket / Detalle final de la Orden
    print(f"\n--- Detalle de la Orden (Mesa {mesa}) ---")
    
    # TODO: Una vez programado 'get_order', iterar sobre él para imprimir la información.
    # Ejemplo de estructura esperada al finalizar:
    # for item in order.get_order():
    #     print(f"• {item.get_dish_info()}")
    
    print(f'------------------------------------------')
    # TODO: Descomentar la línea de abajo una vez programado 'get_total' en la clase Order
    # print(f'TOTAL FINAL: ${order.get_total()}')


# ==========================================
# INTERFAZ DE USUARIO (CLI) Y MENÚ PRINCIPAL
# ==========================================
def main():
    menu = Menu("Restaurant Menu")
    
    while True:
        print('''
==========================================
    SISTEMA DE RESTAURANTE (POO)
==========================================
1 - Llenar el menú
2 - Mostrar el menú
3 - Hacer un pedido
0 - Finalizar el programa
        ''')
        
        choice = input("Ingrese su opción: ")
        
        if choice == '1':
            menu_entry(menu)
        elif choice == '2':
            menu.get_menu()
        elif choice == '3':
            order_entry(menu)
        elif choice == '0':
            print("Programa finalizado. ¡Buen provecho!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()
