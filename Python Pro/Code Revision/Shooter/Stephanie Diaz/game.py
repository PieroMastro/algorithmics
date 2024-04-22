from pygame import *
from random import randint
from time import time

start = time()
timer_1 = start
timer_2 = start + 10  # ¿Qué es el propósito de este temporizador?
spawn_enemy = True

font.init()

font = font.Font(None, 36, bold=True)

img_win = "win.png"
img_los = "" # Actualizar con la imagen correcta
img_back = "galaxy.png"

img_bullet = "bullet.png"
img_hero = "ship.png"
img_enemy = "enemy.png"  # nombre correcto de la imagen

score = 0
goal = 10
lost = 0
max_lost = 5

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < SCREEN_WIDTH - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


SCREEN_WIDTH = 700  # Corrección: SCREEN_WIDHT a SCREEN_WIDTH
SCREEN_HEIGHT = 500
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Shooterrr")
background = transform.scale(image.load(img_back), (SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ship = Player(img_hero, 5, SCREEN_HEIGHT - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, SCREEN_WIDTH - 80), -40, 80, 50, randint(1, 5))  # Corrección: SCREEN_WIDHT a SCREEN_WIDTH
    monsters.add(monster)

# ¿Cuál es el propósito de high_monsters?
high_monsters = sprite.Group()
for u in range(1, 6):
    monster = Enemy(img_enemy, randint(80, SCREEN_WIDTH - 80), -40, 80, 50, randint(1, 10))  # Corrección: SCREEN_WIDHT a SCREEN_WIDTH
    high_monsters.add(monster)

bullets = sprite.Group()
#clock = time.Clock()
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()

    if not finish:  # Esta lógica debe estar dentro de este bloque
        window.blit(background, (0, 0))
        text = font.render(f'Score: {score}', 1, (WHITE))
        window.blit(text, (10, 20))
        text_lose = font.render(f'Enemies lost: {lost}', 1, (RED))  # Corrección: dont.render a font.render
        window.blit(text_lose, (10, 40))  # Incrementa el valor de y para evitar que el texto se solape

        ship.update()
        monsters.update()
        bullets.update()

        bullets.draw(window)
        ship.reset()
        monsters.draw(window)
        if timer_1 == timer_2:
            high_monsters.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)  # Corrección: monsters en lugar de monster

        for c in collides:
            score += 1
            monster = Enemy(img_enemy, randint(80, SCREEN_WIDTH - 80), -40, 80, 50, randint(1, 5))  # Corrección: SCREEN_WIDHT a SCREEN_WIDTH
            monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            img = image.load(img_los)
            d = img.get_width() // img.get_height()
            window.fill((219, 199, 22))
            window.blit(transform.scale(img, (SCREEN_HEIGHT * d, SCREEN_HEIGHT)), (90, 0))

        if score >= goal:
            finish = True
            img = image.load(img_win)
            window.fill(WHITE)
            window.blit(transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

        display.update()

    #time.delay(20)
    #clock.tick(60)

quit()
