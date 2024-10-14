# Definir una clase para el caso de WoC
class Pricelist():
    def __init__(self, name:str):
        self.name = name
        self.pricelist = dict()
        
    def add_price(self, service:str, price:int):
        self.pricelist[service] = price


# Modificando el metodo con numero variable de argumentos
class PriceList():
    def __init__(self, name:str):
        self.name = name
        self.pricelist = dict()
    
    def add_price(self, **kwargs):
        for key in kwargs:
            self.pricelist[key] = kwargs[key]

# ======================================================== #

my_offer = PriceList('Instagram')
my_offer.add_price(stories=100, managements=1000)

print(my_offer.pricelist)