# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  DEMO, SETUP & GAMELOOP + EVENT HANDLING                  #
#  CODIGO CON HERENCIA DE LA CLASE SPRITE (Y COLISIONES)    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from pygame import *

# Inicialización de Pygame
init()

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 20

# Crear la ventana
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Demo')

# Definir una clase que hereda de la clase Sprite
class MySprite(sprite.Sprite):
    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase padre
        self.image = Surface((50, 50))  # Crear una superficie de 50x50 píxeles
        self.image.fill((255, 0, 0))  # Llenar la superficie con color rojo
        self.rect = self.image.get_rect()  # Obtener el rectángulo de la superficie
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Centrar el rectángulo en la pantalla

    def move(self, keys):
        if keys[K_LEFT] and self.rect.x > 15:
            self.rect.x -= SPEED
        if keys[K_RIGHT] and self.rect.x < 730:
            self.rect.x += SPEED
        if keys[K_UP] and self.rect.y > 15:
            self.rect.y -= SPEED
        if keys[K_DOWN] and self.rect.y < 530:
            self.rect.y += SPEED

# Definir una clase para los obstáculos
class Obstacle(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Crear una instancia de la clase MySprite
cuadrado = MySprite()

# Crear instancias de los obstáculos
obstacle1 = Obstacle(200, 200, 100, 100)
obstacle2 = Obstacle(400, 300, 100, 100)

# Agrupar los sprites en un grupo
all_sprites = sprite.Group()
all_sprites.add(cuadrado, obstacle1, obstacle2)

# Bucle principal del juego
run = True
clock = time.Clock()

while run:
    
    window.fill((255, 255, 255))  # Llenar la pantalla con color blanco

    # Manejo de eventos
    for e in event.get():
        if e.type == QUIT:
            running = False

    # Obtener el estado del teclado
    keys = key.get_pressed()

    # Mover el sprite
    cuadrado.move(keys)

    # Verificar colisiones con los obstáculos
    if sprite.spritecollide(cuadrado, all_sprites, False):
        print("¡Colisión!")

    # Dibujar todos los sprites en la pantalla
    all_sprites.draw(window)

    # Actualizar la pantalla
    display.update()

    # Limitar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
quit()
