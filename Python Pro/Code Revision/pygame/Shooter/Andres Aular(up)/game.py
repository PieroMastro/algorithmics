# Importación pygame
from pygame import *
from random import randint

# Inicializar Pygame
init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = display.set_mode((screen_width, screen_height))
display.set_caption("shooter against zombies")

# Clase padre para los objetos del juego
class GameObject:
    def __init__(self, x, y, width, height, speed, object_image):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(object_image), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        pass

# Clase para el jugador
class Player(GameObject):

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.x < screen_width - self.width:
            self.rect.x += self.speed

# Clase para los enemigos
class Enemy(GameObject):

    def move(self):
        self.rect.y += self.speed

# Clase para los disparos
class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 10, 7, "bala.png")

    def move(self):
        self.rect.y -= self.speed

player = Player(screen_width // 2 - 25, screen_height - 60, 50, 50, 3, 'francotiador.png')
enemies = []
bullets = []
score = 0
font = font.SysFont(None, 36)

clock = time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))

    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == KEYDOWN and e.key == K_SPACE:
            bullets.append(Bullet(player.rect.x + player.width // 2 - 2, player.rect.y))

    keys = key.get_pressed()
    if keys[K_LEFT]:
        player.move_left()
    if keys[K_RIGHT]:
        player.move_right()

    # Generar enemigos aleatorios
    if len(enemies) < 5:
        enemy_x = randint(0, screen_width - 50)
        enemy_y = randint(-screen_height, 0)
        enemies.append(Enemy(enemy_x, enemy_y, 50, 50, 3, 'enemigo.png'))


    # Mover y dibujar enemigos
    for enemy in enemies:
        enemy.move()
        screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))

    # Mover y dibujar disparos
    for bullet in bullets:
        bullet.move()
        screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))

    # Colisiones entre disparos y enemigos
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.x < enemy.rect.x + enemy.width and bullet.rect.x + bullet.width > enemy.rect.x and bullet.rect.y < enemy.rect.y + enemy.height and bullet.rect.y + bullet.height > enemy.rect.y:
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10  # Sumar al puntaje en lugar de asignar un valor fijo

    # Colisión entre jugador y enemigos
    for enemy in enemies[:]:
        if player.rect.x < enemy.rect.x + enemy.width and player.rect.x + player.width > enemy.rect.x and player.rect.y < enemy.rect.y + enemy.height and player.rect.y + player.height > enemy.rect.y:
            enemies.remove(enemy)
            # Aquí puedes restar vidas o manejar la colisión de otra manera según tu lógica de juego

    # Mover y dibujar jugador
    screen.blit(player.image, (player.rect.x, player.rect.y))

    # Mostrar puntaje en pantalla
    text = font.render("Puntaje: " + str(score), True, (255, 0, 0))
    screen.blit(text, (10, 10))

    display.flip()
    clock.tick(30)

quit()
