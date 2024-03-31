from time import sleep

class Hero():
    #constructor de clase
    def __init__(self, name: str, health: int, armor: int, weapon: str) -> None:
        self.name = name
        self.health = health 
        self.armor = armor
        self.weapon = weapon
    #imprimir parámetros de personaje
    def print_info(self) -> None:
        print('Nivel de salud:', self.health)
        print('Clase de armadura:', self.armor, '\n')

#luego programa las clases derivadas de la superclase Hero

class Warrior(Hero):
    power = 15

    def hello(self):
        print(f'-> NUEVO HEROE. Un valiente guerrero aparece montado en su caballo y su nombre es {self.name}')
        self.print_info()

    def attack(self, enemy):
        print(f'-> GOLPE! El valiente guerrero {self.name} esta atacando a {enemy.name} con su {self.weapon}')

        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
    
        print(f'Un golpe terrible al enemigo!\nAhora su armadura: {enemy.armor}, y nivel de salud: {enemy.health}\n')
        sleep(3)
        
class Mage(Hero):
    spell_power = 30

    def hello(self):
        print(f'-> NUEVO HEROE. De la nada un habilidoso hechicero aparece, su nombre es {self.name}')
        self.print_info()

    def launch_spell(self, enemy):
        print(f'-> GOLPE! El hechicero {self.name} lanza un poderozo hechizo con su {self.weapon} a {enemy.name}')

        enemy.armor -= self.spell_power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(f'Un complicado hechizo aturde al enemigo!\nAhora su armadura: {enemy.armor}, y nivel de salud: {enemy.health}\n')
        sleep(3)

massi = Warrior('Massimo', 100, 50, 'Espada')
mica = Mage('Micaela', 50, 30, 'Varita')
massi.hello()
mica.hello()
massi.attack(mica)
mica.launch_spell(massi)
