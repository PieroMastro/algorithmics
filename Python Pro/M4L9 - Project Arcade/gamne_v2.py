# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 2.0                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importar los módulos necesarios
from pygame import *
from random import randint

# Inicializando modulo pygame
init()
# estableciendo formato para fuente
font = font.Font(None, 72)

# Variables globales (ajustes)
# Main Screen
SCREEEN_WIDTH, SCREEEN_HEIGHT = 800, 600

# Límites que el jugador no supera (el fondo empieza a moverse)
LEFT_BOUND = SCREEEN_WIDTH / 40
RIGHT_BOUND = SCREEEN_WIDTH - 8 * LEFT_BOUND
SHIFT = 0

X_START, Y_START = 20, 10

# Assets
backgroundGROUND_IMG = 'cave.png'
HERO_IMG = 'm1.png'
ENEMY_IMG = 'enemy.png'
BOMB_IMG = 'bomb.png'
PRINCESS_IMG = 'princess.png'
FPS = 60

# Colores:
WHITE = (255, 255, 255)
DARK = (48, 48, 0)
YELLOW = (255, 255, 87)
GREEN = (32, 128, 32)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# DEFINICION DE CLASES ***REFACTORIZAR****
# Clase primaria
class FinalSprite(sprite.Sprite):
    # Constructor de clase
    def __init__(self, player_image, player_x, player_y, player_speed):
        # Llamando al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # Cada objeto debe almacenar la propiedad image
        self.image = transform.scale(image.load(player_image), (60, 120))
        self.speed = player_speed

        # Cada objeto debe almacenar la propiedad Rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


class Hero(sprite.Sprite): # REFACTORIZAR, HACER DERIVADA DE MainSprite
    def __init__(self, filename, x_speed=0, y_speed=0, x=X_START, y=Y_START, width=120, height=120):
        sprite.Sprite.__init__(self)
        # La imagen es subida de un archivo y encaja en un rectángulo del tamaño correcto:
        self.image = transform.scale(image.load(filename), (width, height)).convert_alpha()
                                        # Utilizamos convert_alpha, lo necesitamos para la transparencia

        # Cada objeto debe almacenar una propiedad rect. Esta propiedad es necesaria para detectar el contacto del objeto.
        self.rect = self.image.get_rect()
        # Colocamos al personaje en un punto específico (x, y):
        self.rect.x = x
        self.rect.y = y
        # Creamos las propiedades y registramos los valores transferidos:
        self.x_speed = x_speed
        self.y_speed = y_speed
        # Agregamos la propiedad stands_on | es la plataforma en la cual está parado el personaje
        self.stands_on = False # Si no está en una, entonces el valor es falso

    def gravitate(self):
        self.y_speed += 0.25

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y


    def update(self):
        ''' Mueve al personaje usando la velocidad actual horizontal y vertical'''
        # primer movimiento horizontal
        self.rect.x += self.x_speed
        # si vamos detrás de la pared, estaremos contra la pared
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # si vamos a la derecha, el borde derecho del personaje está en contra del borde izquierdo de la pared
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # Si tocamos varios al mismo tiempo, el borde derecho es el mínimo
        elif self.x_speed < 0: # yendo a la izquierda, colocamos el borde izquierdo del personaje contra el borde derecho de la pared
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # si varias paredes son tocadas, el borde izquierdo es el máximo


        # ahora el movimiento vertical       
        self.gravitate()
        self.rect.y += self.y_speed
        # si vamos más allá de la pared, estaremos parados contra la pared
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # bajando
            for p in platforms_touched:
                self.y_speed = 0
                # Comprobamos cuál de las plataformas está más alto desde la parte inferior, la alineamos y la registramos como nuestro soporte:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                    self.stands_on = p
        elif self.y_speed < 0: # subiendo
            self.stands_on = False # subimos, ¡lo que significa que ya no estamos parados en nada!
            for p in platforms_touched:
                self.y_speed = 0  # al colisionar con una pared, la velocidad vertical se disipa
                self.rect.top = max(self.rect.top, p.rect.bottom) # alineamos el borde superior con los bordes inferiores de las paredes con las cuales colisionamos


class Wall(sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=GREEN):
        sprite.Sprite.__init__(self)
        # imagen – un nuevo rectángulo del tamaño correcto:
        self.image = Surface([width, height])
        self.image.fill(color)

        # creamos una propiedad rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(sprite.Sprite): # Clase para enemigos
    def __init__(self, x=20, y=0, filename=ENEMY_IMG, width=100, height=100):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(filename), (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Mueve el personaje usando la velocidad horizontal y vertical actual
        self.rect.x += randint(-5, 5)
        self.rect.y += randint(-5, 5)


# Ventana principal
display.set_caption("ARCADE")
window = display.set_mode([SCREEEN_WIDTH, SCREEEN_HEIGHT])
background = transform.scale(image.load(backgroundGROUND_IMG).convert(), (SCREEEN_WIDTH, SCREEEN_HEIGHT))

# Lista de todos los personajes en el juego:
all_sprites = sprite.Group()
# Lista de obstáculos:
barriers = sprite.Group()
# Lista de enemigos:
enemies = sprite.Group()
# Lista de minas:
bombs = sprite.Group()


# Creamos un personaje y lo añadimos a la lista de objetos:
link = Hero(HERO_IMG)
all_sprites.add(link)
# Creamos paredes y las añadimos:
w = Wall(50, 150, 480, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 50, 50, 360)
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 380, 640, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(-200, 590, 1600, 20)
barriers.add(w)
all_sprites.add(w)


# Creamos enemigos y los añadimos:
en = Enemy(50, 480)
all_sprites.add(en)
enemies.add(en)


en = Enemy(400, 480)
all_sprites.add(en)
enemies.add(en)


# creamos minas y las añadimos:
bomb = Enemy(550, 520, BOMB_IMG, 60, 60)
bombs.add(bomb) # no añadimos bombas a la lista de objetos, las dibujaremos con un comando separado
                # Podemos detonar bombas fácilmente y también hacer que estén inmóviles, update() no es llamado


# Creamos el objeto final y lo añadimos:
pr = FinalSprite(PRINCESS_IMG, SCREEEN_WIDTH + 500, SCREEEN_HEIGHT - 150, 0)
all_sprites.add(pr)


# Ciclo principal del videojuego:
run = True
finished = False


while run:
    # Procesamiento de eventos
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                link.x_speed = -5
            elif e.key == K_RIGHT:
                link.x_speed = 5
            elif e.key == K_UP:
                link.jump(-7)


        elif e.type == KEYUP:
            if e.key == K_LEFT:
                link.x_speed = 0
            elif e.key == K_RIGHT:
                link.x_speed = 0


    if not finished:
        # moviendo objetos del videojuego
        all_sprites.update()


        # luego, comprobando las reglas del juego
        # comprobando el contacto de bombas:
        sprite.groupcollide(bombs, all_sprites, True, True)
                # si una bomba toca un objeto, se remueve de la lista de bombas y el objeto es removido de all_sprites


        # comprobar el contacto del personaje con los enemigos:
        if sprite.spritecollide(link, enemies, False):
            link.kill() # el método para matar remueve a un objeto de todos los grupos en los cuales está listado


        # comprueba los bordes de la pantalla:
        if (
            link.rect.x > RIGHT_BOUND and link.x_speed > 0
            or
            link.rect.x < LEFT_BOUND and link.x_speed < 0
        ): # al salir a la izquierda o derecha, el cambio es transferido al SHIFT de pantalla
            SHIFT -= link.x_speed 
            # SHIFT general para todos los objetos (bombas por separado, están en otra lista):
            for s in all_sprites:
                s.rect.x -= link.x_speed # el jugador también está en esta lista, así que su movimiento será cancelado visualmente
            for s in bombs:
                s.rect.x -= link.x_speed


        # Renderizado
        # Dibujamos el fondo con el SHIFT
        local_SHIFT = SHIFT % SCREEEN_WIDTH
        window.blit(background, (local_SHIFT, 0))
        if local_SHIFT != 0:
            window.blit(background, (local_SHIFT - SCREEEN_WIDTH, 0))

        # dibujamos todos los objetos en la pantalla antes de comprobar la victoria/derrota
        # si el juego terminó en esta iteración del ciclo, el nuevo fondo será dibujado sobre los personajes
        all_sprites.draw(window) 
        # dibujamos el grupo de bombas de forma separada, de esta forma una bomba que salga del grupo dejará de ser visible automáticamente
        bombs.draw(window)


        # comprobación de victoria y derrota:
        if sprite.collide_rect(link, pr):
            finished = True
            window.fill(BLACK)
            # escribimos texto en la pantalla
            text = font.render("¡GANASTE!", 1, RED)
            window.blit(text, (250, 250))


        # comprobación de derrota:
        if link not in all_sprites or link.rect.top > SCREEEN_HEIGHT:
            finished = True           
            window.fill(BLACK)
            # escribimos texto en la pantalla
            text = font.render("JUEGO TERMINADO", 1, RED)
            window.blit(text, (250, 250))


    display.update()


    # Pausa
    time.delay(20)