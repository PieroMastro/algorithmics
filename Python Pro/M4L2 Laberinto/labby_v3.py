# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 3.0                                              #
#  CODIGO CON CLASES Y HERENCIA SIMPLE (CLASE PRIMARIA)     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from pygame import *

# Clase padre para otros objetos
class GameSprite():
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, player_speed):
    
        # cada objeto debe almacenar la propiedad image
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
    
        # cada objeto debe almacenar la propiedad rect (rectángulo) en la cual es ingresada
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # metodo para dibujar el personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# clase del jugador principal
class Player(GameSprite):
    # metodo que implementar el control de objetos usando los botones de flechas del teclado
        def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.left > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH - 5:
                self.rect.x += self.speed
            if keys[K_UP] and self.rect.top > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - 5:
                self.rect.y += self.speed

# clase del objeto del enemigo    
class Enemy(GameSprite):
    side = "left"
    # movimiento del enemigo
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= SCREEN_WIDTH - 85:
            self.side = "izquierda"
        if self.side == "izquierda":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# clase del elemento de la pared
class Wall():
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
    
        # imagen de la pared – un rectángulo del tamaño y color deseado
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
    
        # cada objeto debe almacenar la propiedad rect (rectángulo)
        self.rect = self.image.get_rect()
        self.rect = Rect(wall_x, wall_y, wall_width, wall_height)
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


# Main Window:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Labyrinth Project')

# Crear paredes
wall1 = Wall(0, 0, 0, SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2, 300, 10)
wall2 = Wall(0, 0, 0, 410, SCREEN_HEIGHT / 2 - SCREEN_HEIGHT / 4, 10, 350)

# Crear objetos (instancias)
pacman = Player('hero.png', 5, SCREEN_HEIGHT - 80, 5)
monster = Enemy('cyborg.png', SCREEN_WIDTH - 80, 200, 5)
final_sprite = GameSprite('pac.png', SCREEN_WIDTH - 85, SCREEN_HEIGHT - 100, 0)

# Variable responsable por cómo termina el juego:
finish = False

# Game Loop:
run = True
while run:

    time.delay(50)
    # Event Handler (comprobando todos los eventos que pueden suceder):

    for e in event.get():
        # Evento del clic del botón "cerrar"
        if e.type == QUIT:
            run = False

    # Comprobamos que el juego no está terminado todavía:
    if not finish:
        # Refrescamos nuestra ventana con cada iteración:
        window.fill((255, 255, 255))

        # Dibujar las paredes:
        wall1.draw_wall()
        wall2.draw_wall()
        
        # Ejecuta el movimiento del objeto:
        pacman.update()
        monster.update()

        # Los actualiza en una nueva ubicación con cada iteración del ciclo:
        pacman.reset()
        monster.reset()
        final_sprite.reset()

    display.update()
