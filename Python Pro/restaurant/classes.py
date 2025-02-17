# Objects
class Dish():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dish = f'{self.name} ({self.quantity}) - {self.price}'

    def get_dish_info(self):
        return self.dish

class Menu():
    def __init__(self, name):
        self.products = list()
        self.name = name
    
    def set_menu(self, dish):
        self.dish = dish
        self.products.append(dish)

    def get_menu(self):
        print(self.name)
        return self.products

class Order():
    total = 0
    def __init__(self, name):
        self.order = list()
        self.name = name
    
    def set_order(self, param1, param2):
        self.param1 = param1
        self.order.append(param1)
        self.param2 = param2
        self.total += int(self.param2)

    def get_order(self):
        print("Comprobación general: ")
        return self.order
    
    def get_total(self):
        print("Total: ")
        return self.total

