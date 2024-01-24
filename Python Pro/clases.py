# 1. Clase con atributos directos:

class Carro():
    marca = 'Toyota'
    modelo = 'Corolla'
    color = "Negro"
    
mi_carro = Carro()

print("Marca:", mi_carro.marca)
print('Modelo:', mi_carro.modelo)
print('Color:', mi_carro.color)

# 2. Clase simple sin constructor:

class Carro():
    marca = 'Toyota'
    modelo = 'Corolla'
    color = "Negro"

    def info(self):
        print("Marca:", self.marca)
        print('Modelo:', self.modelo)
        print('Color:', self.color)

carro_2 = Carro()

# 3. Implementando el metodo constructor __init__():

class Carro():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def info(self):
        print("Marca:", self.marca)
        print('Modelo:', self.modelo)
        print('Color:', self.color)

carro_3 = Carro('Toyota', 'Hilux', 'Blanco')

carro_3.info()

#4. Ejemplo de creacion de clase, metodos e instancia:

class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Nombre del heroe ->', self.name)
        print('Nivel de salud:', self.health)
        print('Armadura:', self.armor)
        print('Poder:', self.power)
        print('Arma:', self.weapon)

    def strike(self, enemy):
        print(f'{self.name} golpea al {enemy.name} con su {self.weapon} y le quita {self.power} puntos de vida!')

warrior = Hero('Piero', 80, 20, 10, 'Espada')
warrior.print_info()
enemy = Hero('Bandido', 50, 10, 5, 'Daga')

warrior.strike(enemy)