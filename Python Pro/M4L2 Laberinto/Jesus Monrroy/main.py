from pygame import *

screen_height = 1080
screen_width = 680

init()

window = display.set_mode((screen_height, screen_width))
display.set_caption('Ball maze')

class GameSprite(sprite.Sprite):
    def __init__(self, play_mage, play_x, play_y, play_sonic):
        super().__init__() # Eliminar self como argumento
        self.mage = transform.scale(image.load(play_mage), (80, 80))
        self.sonic = play_sonic
        self.rect = self.mage.get_rect()
        self.rect.x = play_x
        self.rect.y = play_y
    def reset(self):
        window.blit(self.mage, (self.rect.x, self.rect.y))

class Character(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.sonic
        if keys[K_d] and self.rect.x < screen_width - 80:
            self.rect.x += self.sonic
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.sonic
        if keys[K_s] and self.rect.y > screen_width - 80:
            self.rect.y += self.sonic

class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= screen_width - 85:
            self.side = "left"
        if self.side == "right":
            self.rect.x += self.sonic
        else:
            self.rect.x -= self.sonic

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        sprite.Sprite().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface([self.wall_width, self.wall_height]) 
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect = Rect(wall_x, wall_y, wall_width, wall_height)
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.wall_width, self.wall_height))

wall_1 = Wall(0, 0, 0, screen_width / 2 - screen_width / 3, screen_height / 2, 300, 10)
wall_2 = Wall(0, 0, 0, 410, screen_width / 2 - screen_width / 4, 10, 350)

rat = Character('rat.png', 5, screen_height, 8)
borg = Enemy('cyborg.png', screen_width - 80, 200, 9)
cheese = GameSprite('cheese.png', screen_width - 85, screen_height - 100, 0)

finito = False
playmomento = True
while playmomento:
    time.delay(100)
    
    for e in event.get():
        if e.type == QUIT:
            playmomento = False

    if not finito:
        window.fill((0,255,0))
        wall_1.draw_wall()

    display.update()

quit()