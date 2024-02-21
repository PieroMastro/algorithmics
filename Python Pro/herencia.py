# 1. Ejemplo de herencia, superclase y clases derivadas:

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return "Attacking"


class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self):
        return super().attack() + " with sword"


class Mage(Character):
    def __init__(self, name, health, magic_power):
        super().__init__(name, health)
        self.magic_power = magic_power

    def attack(self):
        return super().attack() + " with magic"


# Crear personajes
warrior = Warrior("Conan", 100, 20)
mage = Mage("Gandalf", 80, 30)

# Mostrar información de los personajes
print('Hero Created:')
print(f"Warrior: {warrior.name}\nHealth: {warrior.health}\nStrength: {warrior.strength}")
print('=====================')
print('Hero Created:')
print(f"Mage: {mage.name}\nHealth: {mage.health}\nMagic Power: {mage.magic_power}")
print('=====================')


# Mostrar cómo atacan los personajes
print("Warrior Attack:", warrior.attack())
print("Mage Attack:", mage.attack())