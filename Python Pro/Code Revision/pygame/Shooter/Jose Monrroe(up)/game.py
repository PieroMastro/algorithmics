from pygame import *
from pygame.font import Font
from random import randint

init()
font.init()
font = font.Font(None, 36, bold= True)
screen_height = 680
screen_width = 1080
background = transform.scale(image.load('Dystopian_city.png'), (screen_width, screen_height))

score = 0
goal = 10
lost = 0
max_lost = 5

white = (255, 255, 255)

window = display.set_mode((screen_width, screen_height))
display.set_caption('Shoot ma balls')

class GameSprite(sprite.Sprite):
    def __init__(self, mage, play_x, play_y, size_x, size_y, sonic):
        sprite.Sprite.__init__(self)
        self.mage = transform.scale(image.load(mage), (size_x, size_y))
        self.sonic = sonic
        self.rect = self.mage.get_rect()
        self.rect.x = play_x
        self.rect.y = play_y

    def reset(self):
        window.blit(self.mage, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.sonic
        if self.rect.y < 0:
            self.kill()
        
class Character(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.sonic
        if keys[K_RIGHT] and self.rect.x < screen_width - 80:
            self.rect.x += self.sonic
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.sonic
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.sonic
        global lost
        if self.rect.y > screen_height:
            self.rect.x = randint(80, screen_width - 80)
            self.rect.y = 0
            lost = lost + 1

# mons = Enemy('charmander.png', randint(80, screen_height - 80), -40, 80, 50, randint(1, 5))
rat = Character('ship.png', 5, screen_height - 100, 80, 100, 10)

mons = sprite.Group()
for i in range(1, 6):
    enemy = Enemy('charmander.png', randint(80, screen_width - 80), -40, 80, 50, randint(1, 5))
    mons.add(enemy)


bullets = sprite.Group()
clock = time.Clock 
# cheese = GameSprite('pixilart-drawing.png',screen_height - 100, screen_width - 85, 0)

finito = False
playmomento = True
while playmomento:
    for e in event.get():
        if e.type == QUIT:
            playmomento = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rat.fire()
    if not finito:
        window.blit(background, (0, 0))

        text = font.render(f'Score: {score}', 1, white)
        window.blit(text, (10,20))

        text_lose = font.render(f'Enemies lost: {lost}', 1, (255, 0, 0))
        window.blit(text_lose, (10,20))

        rat.update()
        mons.update()
        bullets.update()

        rat.reset()
        mons.draw(window)
        bullets.draw(window)
        # cheese.reset()

    display.update()
quit()