from random import randint
from time import sleep

class Hero():
    # Constructor de clase
    def __init__(self, name:str, health:int, armor:int, power:int, weapon:str) -> None:
        self.name = name
        self.health = health # int
        self.armor = armor # int
        self.power = power # int
        self.weapon = weapon # str
        
    # Mostrar información del personaje:
    def print_info(self):
        print('Nombre:' + self.name)
        print('Nivel de salud:', self.health)
        print('Armadura:', self.armor)
        print('Poder de golpe:', self.power)
        print('Arma:', self.weapon, '\n')
        
    # Golpeando otro personaje
    def strike(self, enemy):
        attack = randint(self.power - 5, self.power + 5)
        print(f'-> ¡GOLPE! {self.name} ataca a {enemy.name} con poder {attack}, usando su {self.weapon}\n')
    
        enemy.armor -= attack
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        
        print(enemy.name + ' derrotado.\nClase de armadura soltada para ' + str(enemy.armor) + ',y nivel de salud reducido a ' + str(enemy.health) + '\n')

    # Empezando una pelea
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'ha caído en esta difícil batalla.\n')
                break
            sleep(5)
    
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'ha caído en esta difícil batalla.\n')
                break
            sleep(5)