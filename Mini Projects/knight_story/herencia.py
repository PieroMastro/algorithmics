# Modules & libs import
from random import randint
from time import sleep

# Creating the main class
class Hero():
    def __init__(self, name:str, health:int, armor:int) -> None:
        self.name = name
        self.hp = health
        self.armor = armor

    def show_info(self):
        print(f'Nombre: {self.name}')
        print(f'Nivel de Salud: {self.hp}')
        print(f'Armadura: {self.armor}\n')

# Sub-classes
class Warrior(Hero):
    def __init__(self, name, health, armor, strength):
        super().__init__(name, health, armor)
        self.strength = strength
        
    def hello(self):
        print('Nuevo Warrior:')
        self.show_info()

ganon = Warrior('Ganondorf', 100, 60, 60)
ganon.show_info()