# # # 1. Clase con atributos directos:

# # class Carro():
# #     marca = 'Toyota'
# #     modelo = 'Corolla'
# #     color = "Negro"
    
# # mi_carro = Carro()

# # print("Marca:", mi_carro.marca)
# # print('Modelo:', mi_carro.modelo)
# # print('Color:', mi_carro.color)

# # # 2. Clase simple sin constructor:

# # class Carro():
# #     marca = 'Toyota'
# #     modelo = 'Corolla'
# #     color = "Negro"

# #     def info(self):
# #         print("Marca:", self.marca)
# #         print('Modelo:', self.modelo)
# #         print('Color:', self.color)

# # carro_2 = Carro()

# # # 3. Implementando el metodo constructor __init__():

# # class Carro():
# #     def __init__(self, marca, modelo, color):
# #         self.marca = marca
# #         self.modelo = modelo
# #         self.color = color

# #     def info(self):
# #         print("Marca:", self.marca)
# #         print('Modelo:', self.modelo)
# #         print('Color:', self.color)

# # carro_3 = Carro('Toyota', 'Hilux', 'Blanco')

# # carro_3.info()

# #4. Ejemplo de creacion de clase, metodos e instancia:

# class Character():
#     def __init__(self, name, health, armor, power, weapon):
#         self.name = name
#         self.health = health
#         self.armor = armor
#         self.power = power
#         self.weapon = weapon

#     def print_info(self):
#         print('Nombre del Heroe:', self.name)
#         print('Nivel de salud:', self.health)
#         print('Armadura:', self.armor)
#         print('Poder:', self.power)
#         print('Arma:', self.weapon)

#     def strike(self, enemy):
#         print(f'{self.name} golpea al {enemy.name} con su {self.weapon} y le quita {self.power} puntos de vida!')

# warrior = Character('Piero', 80, 20, 10, 'Espada')
# warrior.print_info()
# enemy = Character('Bandido', 50, 10, 5, 'Daga')

# warrior.strike(enemy)

# 5. Ejemplo de herencia, superclase, clases derivadas y override :

class Character:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Nombre del héroe:', self.name)
        print('Nivel de salud:', self.health)
        print('Armadura:', self.armor)
        print('Poder:', self.power)
        print('Arma:', self.weapon)

    def strike(self, enemy):
        damage = self.power
        print(f'+ {self.name} golpea al {enemy.name} con su {self.weapon} y le quita {damage} puntos de vida!')
        self.attack(enemy, damage)

    def attack(self, enemy, damage):
        damage -= enemy.armor
        if damage < 0:
            damage = 0
        enemy.health -= damage
        if enemy.health <= 0:
            print(f'- El {enemy.name} ha muerto. \nLa batalla ha finalizado, nuestro grupo ha salido victorioso!')
        else:
            print(f'- El {enemy.name} tiene {enemy.health} puntos de vida restantes.')

class Warrior(Character):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

class Mage(Character):
    def __init__(self, name, health, armor, power, weapon, magic_power):
        super().__init__(name, health, armor, power, weapon)
        self.magic_power = magic_power

    def cast_spell(self, enemy):
        spell_power = self.magic_power * 2
        print(f'+ {self.name} lanza un hechizo al {enemy.name} y le quita {spell_power} puntos de vida!')
        self.attack(enemy, spell_power)

class Rogue(Character):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

    def backstab(self, enemy):
        damage = self.power * 3
        print(f'+ {self.name} apuñala al {enemy.name} por la espalda con su {self.weapon} y le quita {damage} puntos de vida!')
        self.attack(enemy, damage)

# Crear instancias de las clases
warrior = Warrior('Arthur', 80, 20, 10, 'Espada')
mage = Mage('Merlín', 70, 15, 8, 'Varita', 20)
rogue = Rogue('VanCleff', 60, 10, 15, 'Daga')

# Imprimir información de los personajes
print(f'================\nNuevo Personaje:')
warrior.print_info()
print(f'================\nNuevo Personaje:')
mage.print_info()
print(f'================\nNuevo Personaje:')
rogue.print_info()

# Crear un enemigo
enemy = Character('Bandido', 50, 10, 5, 'Daga')

# Realizar acciones de los personajes
print(f'================\nNuestra Party se encuentra con un {enemy.name} e inicia la batalla!')
rogue.backstab(enemy)
warrior.strike(enemy)
mage.cast_spell(enemy)



