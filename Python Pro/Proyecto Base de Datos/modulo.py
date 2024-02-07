class Dish():
    def set_dish_information(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dish = self.name + "(" + self.quantity + ")" + " - " + self.price
    def get_dish_information(self):
        return self.dish

class Menu:
    def set_menu_information(self, name):
        self.name = name
        self.products = []
    def set_menu(self, dish):
        self.dish = dish
        self.products.append(self.dish)
    def get_menu(self):
        print(self.name)
        return self.products

class Receipt():
    result = 0
    def set_order_information(self, name):
        self.name = name
        self.order = []
    def set_order(self, parametr1, parametr2):
        self.parametr1 = parametr1
        self.order.append(self.parametr1)
        self.parametr2 = parametr2
        self.result = self.result + int(self.parametr2)
    def get_order(self):
        print("Comprobación general: ")
        return self.order
    def get_result(self):
        print("Total: ")
        return self.result

def menu_entry(name_menu):
    for i in range(question1):
        name = input("Ingrese el nombre del plato: ")
        quantity = input("Ingrese el tamaño de la porción: ")
        price = input("Ingrese el precio de 1 porción: ")
        d = Dish()
        d.set_dish_information(name, quantity, price)
        name_menu.set_menu(d)

def menu_output(name_menu):
    name_menu.get_menu()
    for i in name_menu.products:
        print(i.name + "(" + i.quantity + "g." +")" + " - " + i.price + "$")

def order_entry(name_menu):
    for i in range(question4):
        question = input("Ingrese el nombre del plato: ")
        for j in name_menu.products:
            if j.name == question:
                check.set_order(j, j.price)
    check.get_order()
    for i in check.order:
        print(i.name + "(" + i.quantity + "g." +")" + " - " + i.price + "$")
    check.get_result()
    print(str(check.result) + "$")

breakfast = Menu()
lunch = Menu()
dinner = Menu()
check = Receipt()

breakfast.set_menu_information("Desayunos")
lunch.set_menu_information("Cenas")
dinner.set_menu_information("Almuerzos")
check.set_order_information("Hacer un pedido")
