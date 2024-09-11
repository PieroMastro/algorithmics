from time import sleep
from characters import Hero


knight = Hero('Richard', 50, 25, 20, 'espada')
dragon = Hero('Dragón', 100, 25, 10, 'flama')


print('¡La Tierra Media está en peligro! Un caballero valiente se apresura para rescatarla...')
knight.print_info()


sleep(2)
print(knight.name + ' está atravesando el bosque. De repente, ve a un ladrón mezquino en el camino...')


sleep(2)
rascal = Hero('Peter', 20, 5, 5, 'cuchillo')
rascal.print_info()


sleep(2)
if input('¿Pelear? (sí/no) >>') == 'sí':
    print('\n¡QUÉ EMPIECE LA PELEA!\n')
    sleep(2)
    knight.fight(rascal)
    sleep(2)


if knight.health > 0:
    knight.health = 100
    knight.power *= 2
    knight.armor = 10*2
    print('\n' + knight.name + ' recuperó su poder y se volvió más experimentado. Ahora, el poder de su golpe es: ' + str(knight.power) + ', y la clase de armadura:' + str(knight.armor) + '\n')


sleep(2)
print('\nFinalmente ' + knight.name + ' llega al calabozo.')
dragon.print_info()


print('\n¡QUÉ EMPIECE LA PELEA!\n')
sleep(2)
knight.fight(dragon)
