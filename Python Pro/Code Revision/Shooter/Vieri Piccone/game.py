from random import randint
from pygame import *

init()

# Configuración inicial
cantEnemigos = 7
max_score = 0
max_lost = 3
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
derrota_image = image.load('derrota.png')

# Clase padre para los otros objetos
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Clase del jugador principal
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.speed

    def fire(self, bullets):
        bullet = Bullet('RayoSinFondo.png', self.rect.centerx - 75, self.rect.top, 150, 75, 15)
        bullets.add(bullet)

# Clase de objeto enemigo    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += randint(1, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = randint(-100, -40)

# Clase de bala
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Clase de elemento de la pared
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.image = Surface([wall_width, wall_height])
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Crear una ventana
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Tirador")
background = transform.scale(image.load('backgroundVSC.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Crear objetos
mano = Player('sanic.png', SCREEN_WIDTH // 2.3, (SCREEN_HEIGHT // 2) + 250, 80, 120, 11)

# Grupo de enemigos
piezas = sprite.Group()
for _ in range(cantEnemigos):
    new_enemy = Enemy("meteoritosinfondo.png", randint(0, SCREEN_WIDTH - 80), randint(-100, -40), 80, 50, randint(1, 5))
    piezas.add(new_enemy)

# Grupo de balas
bullets = sprite.Group()
clock = time.Clock()

# Variable para el estado del juego
finish = False
run = True

# Ciclo de juego
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                mano.fire(bullets)

    if not finish:
        collides = sprite.groupcollide(piezas, bullets, True, True)
        for _ in collides:
            max_score += 1
        
        window.blit(background, (0, 0))
        
        # Movimiento y actualización
        mano.update()
        piezas.update()
        bullets.update()
        
        # Dibujar los objetos en la ventana
        mano.reset(window)
        piezas.draw(window)
        bullets.draw(window)
        
        # Mostrar puntaje
        score_text = font.Font(None, 36).render(f"Puntaje: {max_score}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))
        
        if sprite.spritecollide(mano, piezas, False):
            window.blit(derrota_image, (0, 0))
            display.flip()
            finish = True

    display.update()
    clock.tick(144)

quit()

