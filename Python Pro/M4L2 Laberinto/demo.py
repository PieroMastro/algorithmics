from pygame import *
from random import randint

init() # init pygame

# define constants for colors and screen size
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

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, speed):
        super().__init__()
        # cada objeto debe almacenar la propiedad image-su imagen
        self.image = transform.scale(image.load(sprite_image), (SPRITE_WIDTH, SPRITE_HEIGHT))
        # cada objeto debe almacenar la propiedad rect- el rectángulo en el cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < SCREEN_WIDTH - SPRITE_WIDTH:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < SCREEN_HEIGHT - SPRITE_HEIGHT:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, sprite_image, x, y, speed):
        super().__init__(sprite_image, x, y, speed)
        self.facing_right = True  # Track enemy's direction (initially facing right)
        self.original_image = self.image  # Store the original image

    def update(self):
        if self.facing_right:
            self.rect.x += self.speed
            if self.rect.x >= SCREEN_WIDTH - SPRITE_WIDTH:
                self.facing_right = False
                self.image = transform.flip(self.original_image, True, False)  # Flip horizontally
        else:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.facing_right = True
                self.image = transform.flip(self.original_image, False, False)  # Load original image
        

player = Player('hero.png', 200, 200, 5)
enemy = Enemy('cyborg.png', 600, 200, 5)

run = True
finish = False
clock = time.Clock()

while run:
    time.delay(20)
    clock.tick(120)
    # main event
    for e in event.get():
            
        if e.type == QUIT:
            run = False

    if not finish:
        # update screen
        window.fill(BLACK)
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()

    display.update()

quit()












        # check collision and change color
        # color = GREEN
        #if square.colliderect(obstacle):
            #color = RED
            #finish = True
            #window.fill(BLACK)
            #game_over = image.load('game-over_2.png')
            #window.blit(transform.scale(game_over, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
            
        # get mouse coordinates and use them to position the rectangle
        #position = mouse.get_pos()
        #square.center = position