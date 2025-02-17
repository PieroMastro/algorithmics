from classes import *

# Logic
def meny_entry(menu_name, num):
    for i in range(num):
        name = input("Ingrese el platillo: ")
        quantity = input("Ingrese el tamaño de la porción: ")
        price = input("Ingrese el precio de 1 porción: ")
        dish = Dish(name, quantity, price)
        menu_name.set_menu(dish)

def check_menu(menu_name):
    menu_name.get_menu()
    for item in menu_name.products:
        print(f'{item.name} ({item.quantity}.g) - ${item.price}')
            
def order_entry(menu_name, num):
    for i in range(num):
        question = input('Ingrese el platillo: ')
        for item in menu_name.products:
            if item.name == question:
                check.set_order(iten, item.price)
    check.get_order()
    for item in check.order:
        print(f'{item.name} ({item.quantity}.g) - ${item.price}')
    check.get()
    print(f'Total: ${check.total}')