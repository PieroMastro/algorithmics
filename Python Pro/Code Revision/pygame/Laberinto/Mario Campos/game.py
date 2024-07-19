# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  UPDATE 1 | Player movement y enemy rendering             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from pygame import *

init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_WIDTH = 80
SPRITE_HEIGHT = 80
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


window = display.set_mode((800, 600))

display.set_caption("laberinto")

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, speed):
        super(). __init__()

        self.image = transform.scale(image.load(sprite_image), (SPRITE_WIDTH, SPRITE_HEIGHT)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < SCREEN_WIDTH - SCREEN_WIDTH: # Cambio SCREEN_WIDTH por SPRITE_WIDTH para establecer el limite derecho
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < SCREEN_WIDTH + SCREEN_HEIGHT:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, sprite_image, x, y, speed=0):
        super().__init__ (sprite_image, x, y, speed)
        self.facing_right = True
        self.original_image = self.image

    def update(self):
        if self.facing_right:
            self.rect.x += self.speed
            if self.rect.x >= SCREEN_WIDTH - SPRITE_WIDTH:
                self.facing_right = False
                self.image = transform.flip(self.original_image, True, False) 
        else:
            self.rect.x -= self.speed
            if self.rect.x <= 1:
                self.facing_right = True
                self.image = transform.flip(self.original_image, False, False)
class Wall(sprite.Sprite):
    def __init__ (self, color, wall_x, wall_y, wall_width, wall_height):
        super(). __init__ ()
        self.color = color
        self.width = wall_width
        self.height = wall_height

        self.image = Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        draw.rect(window,
            self.color,
            (self.rect.x, self.rect.y, self.width, self.height)
            )


player = Player("hero.png", 100, 100, 5)
enemy = Enemy("football.png", 100, 500, 5)
enemy_1 = Enemy("football.png", 100, 300, 5)
wall_1 = Wall(WHITE, SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3, SPRITE_HEIGHT / 1, 500, 50)
wall_2 = Wall(WHITE, SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3, SPRITE_HEIGHT / 4, 50, 500)
    
run = True
finish = False
clock = time.Clock()

while run:
    time.delay(20)
    clock.tick(120)

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
    
        window.fill(BLACK)

        wall_1.draw_wall()
        wall_2.draw_wall()

        player.update()
        player.reset()

        enemy.update()
        enemy_1.update()
        enemy.reset()
        enemy_1.reset() # Llamar al metodo correcto para renderizar en pantalla el enemigo

    if sprite.collide_rect(player, enemy):
        finish = True
        window.fill(WHITE)
        img = image.load("game-over_2.png")
        window.blit(transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


    display.update()

quit()


