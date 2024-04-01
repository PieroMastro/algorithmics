# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 5.0 - FINAL                                      #
#  CODIGO CON HERENCIA DE LA CLASE SPRITE (CON COLISIONES)  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from pygame import *

init() # init pygame

# Definir constantes para colores y tamaños de pantalla/objetos
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_WIDTH = 80
SPRITE_HEIGHT = 80
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# main window
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('My First Game')

# Clase padre para los otros objetos
class GameSprite(sprite.Sprite):
    # Constructor de clase
    def __init__(self, sprite_image, x, y, speed):
        # Llama el constructor de clase (Sprite):
        super().__init__() # o sprite.Sprite()
        # cada objeto debe almacenar la propiedad imagen
        self.image = transform.scale(image.load(sprite_image), (SPRITE_WIDTH, SPRITE_HEIGHT))
        # cada objeto debe almacenar la propiedad rect - el rectángulo en el cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed
    # metodo para dibujar el sprite en la pantalla
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Clase del jugador principal
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        # control de objetos utilizando los botones del teclado
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < SCREEN_WIDTH - SPRITE_WIDTH:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < SCREEN_HEIGHT - SPRITE_HEIGHT:
            self.rect.y += self.speed

# Clase de objetos enemigos
class Enemy(GameSprite):
    def __init__(self, sprite_image, x, y, speed):
        super().__init__(sprite_image, x, y, speed)
        self.facing_right = True  # Registra la direccion del objeto (inicia mirando a la derecha)
        self.original_image = self.image  # Guardamos la imagen original

    def update(self):
        if self.facing_right:
            self.rect.x += self.speed
            if self.rect.x >= SCREEN_WIDTH - SPRITE_WIDTH: # Si llega al borde derecho
                self.facing_right = False # Actualizamos nuestro booleano
                self.image = transform.flip(self.original_image, True, False) # Invertimos la imagen horizontalmente
        else:
            self.rect.x -= self.speed
            if self.rect.x <= 430: # Si llega al borde izquierdo
                self.facing_right = True
                self.image = transform.flip(self.original_image, False, False)  # Cargamos la imagen original (revertimos el flip)
        
# Clase de elementos de paredes
class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color # debemos definir los colores para que funcione
        self.width = wall_width
        self.height = wall_height

        # Imagen de la pared - un rectángulo de tamaño y color deseado
        self.image = Surface([self.width, self.height]) # Creamos una instancia de Surface, del ancho y alto deseado
        self.image.fill(self.color) # Con el metodo fill() implementamos el color del objeto
        # cada objeto debe almacenar la propiedad rect (rectángulo)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    # metodo que dibuja un rectangulo en nuestra ventana
    def draw_wall(self):
        draw.rect(
            window,
            self.color,
            (self.rect.x, self.rect.y, self.width, self.height)
            )

# Crear instancias de objetos (sprites)
player = Player('hero.png', 200, 200, 5)
enemy_1 = Enemy('cyborg.png', 700, 150, 3)
enemy_2 = Enemy('cyborg.png', 430, 450, 3)
goal = GameSprite('pac.png', SCREEN_WIDTH - SPRITE_WIDTH, SCREEN_HEIGHT - SPRITE_HEIGHT, 0)

# Crear paredes
wall_1 = Wall(WHITE, SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2, 300, 10)
wall_2 = Wall(RED, 425, SCREEN_HEIGHT / 2 - SCREEN_HEIGHT / 4, 10, 400)

run = True # variable que establece nuestro main loop
finish = False # variable responsable de finalizar el juego
clock = time.Clock() # variable para designar un objeto clock

# Ciclo de juego
while run:
    time.delay(20) # el ciclo se ejecuta cada 0.02 segundos
    clock.tick(120) # se asigna el framerate (numero de cuadros por segundo)
    
    # se revisa todos los eventos que pueden suceder
    for e in event.get():
        # evento de clic en el botón “cerrar”    
        if e.type == QUIT:
            run = False

    # comprueba que el juego no ha terminado todavía
    if not finish:
        # actualiza el fondo con cada iteración
        window.fill(BLACK)
        # dibuja las paredes
        wall_1.draw_wall()
        wall_2.draw_wall()
        # ejecuta el movimiento del objeto
        player.update()
        enemy_1.update()
        enemy_2.update()
        # los actualiza en una nueva ubicación con cada iteración del ciclo
        player.reset()
        enemy_1.reset()
        enemy_2.reset()
        goal.reset()

        # Establecemos las condiciones para que nuestro juego termine (GameOver o Win)
        # comprueba la colisión entre el personaje y el enemigo o las paredes (GAME OVER)
        if sprite.collide_rect(player, enemy_1) or sprite.collide_rect(player, enemy_2) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) :
            finish = True
            window.fill(BLACK)
            img = image.load('game-over_2.png')
            window.fill(BLACK)
            window.blit(transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))

        # comprueba la colisión entre el personaje y el objetivo final (WIN)
        elif sprite.collide_rect(player, goal):
            finish = True
            window.fill(WHITE)
            img = image.load('thumb.jpg')
            window.blit(transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

    display.update()

quit()

