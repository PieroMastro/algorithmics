# 1. Ejemplo de herencia, superclase y clases derivadas:
class Character():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return 'Attacking '

class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self):
        return super().attack() + 'with axes'
    
class Mage(Character):
    def __init__(self, name, health, magic):
        super().__init__(name, health)
        self.magic = magic
        
    def attack(self):
        return super().attack() + 'with Magic'
    
    def fireball(self):
        return 'Throw a fireball'

carlitos = Warrior('Carlitos', 100, 40)
pepe = Mage('Pepe', 50, 80)

print('Heroe creado:')
print(f'Warrior: {carlitos.name}\nHealth: {carlitos.health}\nStrength: {carlitos.strength}')
print(f'{carlitos.name} {carlitos.attack()}')
print('=================================')

print('Heroe creado:')
print(f'Mage: {pepe.name}\nHealth: {pepe.health}\nMagic: {pepe.magic}')
print(f'{pepe.name} {pepe.attack()}')
print(f'{pepe.name} {pepe.fireball()}')

