# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 5.0                                              #
#  CODIGO CON HERENCIA DE LA CLASE SPRITE (CON COLISIONES)  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from pygame import *

# clase padre para los otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, player_speed):
        # Llama el constructor de clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar la propiedad image
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect (rectángulo) en donde es ingresado
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # método de dibujo del personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# clase de jugador principal
class Player(GameSprite):
    # método que implementa el control de objetos utilizando los botones de flechas del teclado
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < SCREEN_WIDTH - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < SCREEN_HEIGHT - 80:
            self.rect.y += self.speed


# clase de objeto enemigo    
class Enemy(GameSprite):
    side = "left"
    #movimiento del enemigo
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= SCREEN_WIDTH - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


# clase de elemento de la pared
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        sprite.Sprite.__init__(self)
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # imagen de la pared – un rectángulo de tamaño y color deseado
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))

        # cada objeto debe almacenar la propiedad rect (rectángulo)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


# crea una ventana
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
display.set_caption("Labyrinth")
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# crea paredes
wall1 = Wall(0, 0, 0, SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2, 300, 10)
wall2 = Wall(0, 0, 0, 410, SCREEN_HEIGHT / 2 - SCREEN_HEIGHT / 4, 10, 350)

# crea objetos
pacman = Player('hero.png', 5, SCREEN_HEIGHT - 80, 5)
monster = Enemy('cyborg.png', SCREEN_WIDTH - 80, 200, 5)
final_sprite = GameSprite('pac.png', SCREEN_WIDTH - 85, SCREEN_HEIGHT - 100, 0)

# variable para designar un objeto clock
clock = time.Clock()

# variable responsable por cómo termina el juego
finish = False

# ciclo de juego
run = True
while run:
    # el ciclo se ejecuta cada 0.05 segundos
    time.delay(50)
    # se asigna el framerate (numero de cuadros por segundo)
    clock.tick(60)

    # se revisa todos los eventos que pueden suceder
    for e in event.get():
        # evento de clic en el botón “cerrar”
        if e.type == QUIT:
            run = False

    # comprueba que el juego no ha terminado todavía
    if not finish:
        # actualiza el fondo con cada iteración
        window.fill((255, 255, 255))
        # dibuja las paredes
        wall1.draw_wall()
        wall2.draw_wall()
        # ejecuta el movimiento del objeto
        pacman.update()
        monster.update()
        # los actualiza en una nueva ubicación con cada iteración del ciclo
        pacman.reset()
        monster.reset()
        final_sprite.reset()

        # comprueba la colisión entre el personaje y el enemigo o las paredes
        if sprite.collide_rect(pacman, monster) or sprite.collide_rect(pacman, wall1) or sprite.collide_rect(pacman, wall2):
            finish = True
            # calcula la tasa
            img = image.load('game-over_1.png')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (SCREEN_HEIGHT * d, SCREEN_HEIGHT)), (90, 0))

        if sprite.collide_rect(pacman, final_sprite):
            finish = True
            img = image.load('thumb.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

    display.update()
