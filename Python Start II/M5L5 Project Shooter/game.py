# VERSION 1.0
from pygame import *

init()

# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
BACKGROUND_IMG = 'galaxy.jpg'
PLAYER_IMG = 'rocket.png'
ENEMY_IMG = 'ufo.png'
MUSIC = 'space.ogg'
FPS = 60

# Main Window
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Project Shooter Python Start II')
background = transform.scale(image.load(BACKGROUND_IMG), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Game Music
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

# Main Class
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x_pos, y_pos, width, height, speed= 0) -> None:
        super().__init__()

        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Player Class
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x <= SCREEN_WIDTH - 70:
            self.rect.x += self.speed
            
    def fire(self):
        pass

# Objects
player = Player(PLAYER_IMG, (SCREEN_WIDTH - 65) // 2, SCREEN_HEIGHT - 80, 65,65, 5)

# Main Game
run = True
clock = time.Clock()

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background, (0,0))
    player.reset()
    player.update()

    display.update()
    clock.tick(FPS)

quit()