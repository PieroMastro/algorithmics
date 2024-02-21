from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Inicialización de Pygame
init()

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
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_UP]:
            self.rect.y -= 5
        if keys[K_DOWN]:
            self.rect.y += 5

# Crear una instancia de la clase MySprite
cuadrado = MySprite()

# Bucle principal del juego
running = True
clock = time.Clock()

while running:
    window.fill((255, 255, 255))  # Llenar la pantalla con color blanco

    # Manejo de eventos
    for e in event.get():
        if e.type == QUIT:
            running = False

    # Obtener el estado del teclado
    keys = key.get_pressed()

    # Mover el sprite
    cuadrado.move(keys)

    # Dibujar el sprite en la pantalla
    window.blit(cuadrado.image, cuadrado.rect)

    # Actualizar la pantalla
    display.update()

    # Limitar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
quit()
