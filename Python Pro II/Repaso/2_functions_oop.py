# FUNCTIONS:
# def success(data):
#     if data >= 4.0:
#         return 'El lanzamiento del startup fue un éxito'
#     elif data < 4.0 and data > 3.0:
#         return 'El lanzamiento del startup estuvo bien'
#     return 'El proyecto necesita más trabajo'

# rate = float(input('Calificación de la app'))
# print(success(rate))

# def get_price(number_of_guests):
#     price_per_guests = 10
#     total_cost = number_of_guests * price_per_guests
#     if number_of_guests > 100:
#         total_cost *= 0.9
#     return total_cost

# presupuesto = int(input('Cuantos invitados?'))
# print('Su presupuesto para la fiesta es de',get_price(presupuesto))

# Lambda Function: Es una funcion anonima que se utliza en 1 sola linea para efectos de practicidad, solo puede tener una expresion

# multiplicar_lambda = lambda a, b: a * b

# def multiplicar(a,b):
#     return a * b

# a = int(input('ingrese un numero'))
# b = int(input('ingrese un numero'))
# print('el resultado es (funcion regular):', multiplicar(a,b))
# print('el resultado es (utilizando lambda):', multiplicar_lambda(a,b))


   # EJEMPLO
# """
# In this example you can see how your code gets a lot
# more organized when you separate it into smaller functions
# """

# peoplesGenre = ["m","m","m","f","m","m","f","m","f","f","f"]
# peoplesAges  = [23,45,12,19,40,29,56,70,17,26,29]
# peoplesNames = ["Tom","Rob","Emre","Liv","Ale","Bob","Alice","Jake","Yin","Kim","Lesly"]

# def get_average(ages):
# 	sum = 0
# 	#sum all the ages
# 	for age in ages:
# 		sum += int(age)
# 	# divide between the total number of ages
# 	return str(round(sum/len(ages)))

# def get_youngest(ages):
# 	# sort the array
# 	ages.sort()
# 	# return the first item because its sorted from small to big
# 	return str(ages[0])

# def get_person_info(name):
# 	for i in range(0,len(peoplesNames)):
# 		if name == peoplesNames[i]:
# 			return "Name: " + name + ", age: "+str(peoplesAges[i])+", genre: "+peoplesGenre[i]

# print("We have an average age of " + get_average(peoplesAges))
# print("The youngest person has " + get_youngest(peoplesAges) + " years old")
# print("Here is Tom information -> "+get_person_info("Tom"))
# print("Here is Alice information -> "+get_person_info("Alice"))

# +++++ PROGRAMACION ORIENTADA A OBJETOS +++++
'''Una clase es una plantilla para crear objetos. 
Los objetos tienen atributos (variables) y métodos (funciones) que se definen en la clase. 
Para crear una clase, se utiliza la palabra clave class, seguida del nombre de la clase y dos puntos.'''

# class Persona:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         print(f"Hola, mi nombre es {self.nombre}.")

# # Crear un objeto de la clase Persona
# p = Persona("Juan")
# p.saludar()  # Imprime "Hola, mi nombre es Juan."

'''Implementacion del caso de WoC'''
class Price_list():
    def __init__ (self, name ):
        self.name = name
        self.pricelist = dict()
    def add_price(self, product, price):
        self.pricelist[product] = price

my_offer = Price_list('Servicios para Instagram')
my_offer.add_price('Stories', 100)
