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

carlitos = Warrior('Carlitos', 100, 40)

print('Heroe creado:')
print(f'Warrior: {carlitos.name}\nHealth: {carlitos.health}\nStrength: {carlitos.strength}')
print(f'{carlitos.name} {carlitos.attack()}')

