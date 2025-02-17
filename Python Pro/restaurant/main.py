# CLASSES
class Dish():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def get_dish_info(self):
        return f'{self.name} ({self.quantity}) - ${self.price}'

class Menu():
    def __init__(self, name):
        self.products = []
        self.name = name
    def set_menu(self, dish):
        self.products.append(dish)
    def get_menu(self):
        print(self.name)
        for item in self.products:
            print(item.get_dish_info())

class Order():
    def __init__(self):
        self.order = []
        self.total = 0
    def set_order(self, item):
        self.order.append(item)
        self.total += float(item.price)
    def get_order(self):
        order_info = []
        for item in self.order:
            order_info.append(item.get_dish_info())
        return order_info
    def get_total(self):
        return self.total


# LOGIC
def menu_entry(menu):
    num = int(input("¿Cuántos platillos desea agregar al menú? "))
    for i in range(num):
        name = input("Ingrese el platillo: ")
        quantity = input("Ingrese el tamaño de la porción: ")
        price = input("Ingrese el precio de 1 porción: ")
        dish = Dish(name, quantity, price)
        menu.set_menu(dish)

def order_entry(menu):
    order = Order()
    num = int(input("¿Cuántos platillos desea pedir? "))
    for i in range(num):
        question = input('Ingrese el platillo: ')
        found = False
        for item in menu.products:
            if item.name == question:
                order.set_order(item)
                found = True
                break
        if not found:
            print(f'El platillo "{question}" no está en el menú.')

    print("Su pedido es:")
    for item in order.get_order():
        print(item)
    print(f'Total: ${order.get_total()}')

# INTERFACE
def main():
    print('''
Este es un programa de menú para un restaurante.

Las siguientes acciones están disponibles en él:
    1 - Llenar el menú
    2 - Mostrar el menú
    3 - Hacer un pedido
    0 - Finalizar el programa
    
Para hacer algo, ingrese el número correspondiente.
''')

    menu = Menu("Restaurant Menu")
    
    while True:
        choice = input("Ingrese su opción: ")
        if choice == '1':
            menu_entry(menu)
        elif choice == '2':
            menu.get_menu()
        elif choice == '3':
            order_entry(menu)
        elif choice == '0':
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
