#Definicion de la clase Character
class Character():
    #Class level variable, aplicada a todas las instancias de la clase
    race = 'Human'

    #Medodo constructor de la clase, self hace referencia al objeto actual de la clase, seguida de sus parametros
    def __init__(self, name: str, health: int, damage: int) -> None:
        self.name = name #Atributo del objeto = valor proporcionado al crear la instancia
        self.health = health
        self.max_health = health
        self.damage = damage

        self.weapon = fists #Todas las instancias de Character inician con esta arma

    #Metodo de instancia, toma 2 parametros "self" (referencia al objeto actual) y "target" (objeto que ataca)
    def attack(self, target) -> None: #"None" es una anotacion de tipo, indica que el metodo attack no devuelve ningun valor
        #target.health -= self.damage #Accede al hp del objeto target y le resta self.damage

        #Modificando el metodo para utilizar armas ->
        damage = self.damage + self.weapon.damage
        target.health -= damage
        target.health = max(target.health, 0) #Aseguramos que la salud no sea negativa, en caso de ser asi se establece en cero

        print(f'{self.name} golpea con {self.weapon.name} a {target.name} y le hace {damage} puntos de daño!')

class Hero(Character):
    def __init__(self, name: str, health: int, damage: int) -> None:
        super().__init__(name= name, health= health, damage= damage)

    #Definir metodos para equipar y soltar armas (pendiente)
    

class Enemy(Character):
    def __init__(self, name: str, health: int, damage: int, weapon) -> None:
        super().__init__(name= name, health= health, damage= damage)
        self.weapon = weapon


#Definicion de la clase Weapon
class Weapon():
    def __init__(self,name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

#Creando instancias de nuestras clases (objetos)

iron_sword = Weapon(name = 'Iron Sword', weapon_type= 'sharp', damage= 5, value= 10)
short_bow = Weapon(name = 'Short Bow', weapon_type= 'ranged', damage= 4, value= 8)
fists = Weapon(name = 'Fists', weapon_type= 'blunt', damage= 2, value= 0)

hero = Hero(name= 'Hero', health= 100, damage= 5)
enemy = Enemy(name= 'Enemy', health= 100, damage= 3, weapon= short_bow)


while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f'Health of {hero.name}: {hero.health}')
    print(f'Health of {enemy.name}: {enemy.health}')
    
    input("> ")

    if hero.health == 0 or enemy.health == 0:
        break
