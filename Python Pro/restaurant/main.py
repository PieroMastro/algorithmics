# CLASES
class Dish():
    def __init__(self, dish_id:int, name:str, description:str, price:float):
        self.dish_id = dish_id
        self.name = name
        self.description = description
        self.price = price

    def get_dish_info(self):
        return f'{self.name}: {self.description} - ${self.price}'


class Menu():
    def __init__(self, menu_id:int, name:str):
        self.menu_id = menu_id
        self.name = name
        self.products = list()

    def set_menu(self, item):
        self.products.append(item)
    
    def get_menu(self):
        print(f'- {self.name} -')
        for item in self.products:
            print(item.get_dish_info())
        return self.products

    
class Order():
    def __init__(self, number:int):
        self.number = number
        self.order = list()
        self.total = 0
         
    def set_order(self, item):
        self.order.append(item)
        self.total += float(item.price)

    def get_order(self):
        return self.order
    
    def get_total(self):
        return self.total


# LOGIC
def menu_entry(menu):
    num = int(input("¿Cuántos platillos desea agregar al menú? "))
    for i in range(num):
        dish_id = i + 1
        name = input("Ingrese el platillo: ")
        description = input("Ingrese la descripción del platillo: ")
        price = float(input("Ingrese el precio de 1 porción: ")) 
        dish = Dish(dish_id, name, description, price)
        menu.set_menu(dish)

def order_entry(menu):
    mesa = int(input("Número de mesa: "))
    order = Order(mesa)
    
    num = int(input("¿Cuántos platillos desea pedir? "))
    for i in range(num):
        question = input('Ingrese el nombre del platillo: ')
        found = False
        for item in menu.products:
            if item.name.lower() == question.lower():
                order.set_order(item)
                found = True
                break
        if not found:
            print(f'El platillo "{question}" no está en el menú.')

    print(f"\n--- Detalle de la Orden (Mesa {order.number}) ---")
    
    for item in order.get_order():
        print(f"• {item.get_dish_info()}")
        
    print(f'------------------------------------------')
    print(f'TOTAL FINAL: ${order.get_total()}')


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

main()
