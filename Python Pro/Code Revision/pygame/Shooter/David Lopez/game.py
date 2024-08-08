from pygame import *
from random import *

init()

# CONSTANTES.
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
PLAYER_IMG = "espacial.png" 
ENEMY_IMG = "asteroide.png"
BULLET_IMG = "bala.png"
DEAD_IMG = "derrota.jpg"
WIN_IMG = "victoria.webp"
BACKGROUND = "espacio.jpg"
FPS = 120
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
VIOLET = (180, 0, 180)
LIGHT_GREEN = (180, 180, 0)

font = font.Font(None, 36)  # Fuente por defecto con tamaño 36

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("SHOOTER PROJECT")

background_image = transform.scale(image.load(BACKGROUND), (SCREEN_WIDTH, SCREEN_HEIGHT))  # Carga la imagen de fondo una sola vez

class Caracter(sprite.Sprite):
    def __init__(self, x, y, image_path, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (50, 50))  # Cambiar tamaño según sea necesario
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

    def reset(self, window):
        """Dibuja el personaje en la ventana dada."""
        window.blit(self.image, self.rect.topleft)

class Player(Caracter):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path, speed=5)

    def update(self):
        keys = key.get_pressed()
        self.rect.x += (keys[K_RIGHT] - keys[K_LEFT]) * self.speed
        self.rect.y += (keys[K_DOWN] - keys[K_UP]) * self.speed

        # Asegura que el jugador permanezca dentro de los límites de la pantalla
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def shoot(self):
        """El jugador dispara una bala."""
        bullet = Bullet(self.rect.centerx, self.rect.centery, BULLET_IMG)
        bullets.add(bullet)

class Enemy(Caracter):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path, speed=2)

    def update(self):
        """Actualiza la posición del enemigo."""
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Elimina al enemigo cuando sale de la pantalla

class Bullet(Caracter):
    def __init__(self, x, y, image_path, speed=7):
        super().__init__(x, y, image_path, speed=speed)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

enemies = sprite.Group()
bullets = sprite.Group()
player = Player(100, 550, PLAYER_IMG)
points = 0
clock = time.Clock()
enemy_timer = 0

def create_enemy():
    x = randint(0, SCREEN_WIDTH - 50)  # Posición x aleatoria
    y = -50  # Comienza arriba de la pantalla
    enemy = Enemy(x, y, ENEMY_IMG)
    enemies.add(enemy)

running = True
finish = False

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.shoot()  # El jugador dispara cuando se presiona la barra espaciadora

    player.update()

    # Crear nuevos enemigos a intervalos regulares
    enemy_timer += 1
    if enemy_timer > FPS:
        create_enemy()
        enemy_timer = 0

    bullets.update()
    enemies.update() 

    window.blit(background_image, (0, 0))  # Dibuja la imagen de fondo
    player.reset(window)
    bullets.draw(window)
    enemies.draw(window)


    # Verificar colisiones entre balas y enemigos
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                bullet.kill()
                enemy.kill()
                points += 1  # Incrementa el puntaje

    # Dibujar contador de puntos en la pantalla
    text_surface = font.render(f'Puntos: {points}', True, WHITE)
    window.blit(text_surface, (10, 10))

    display.update()
    clock.tick(60)

quit()