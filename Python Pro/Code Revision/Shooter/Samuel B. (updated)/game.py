from pygame import *
from random import randint


font.init()
font=font.Font(None,64)

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):

        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (80, 80))
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

        
class Enemy(GameSprite):
    side = "Up"
    def update(self):
        if self.rect.y <= 35:
            self.side = "Down"
        if self.rect.y >= SCREEN_WIDTH-85:
            self.side = "Down"
        if self.side == "Down":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Minion(GameSprite):
    #movimiento del enemigo
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = randint(80, SCREEN_WIDTH - 80)
            self.rect.y = 0


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y < 0:
            self.kill()

class Powerups(GameSprite):
    #Terminar

    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
RED=(255,0,0)

score=0
boss_score = 20 
lost= 0
max_lost= 5
goal = 10

display.set_caption("Half life")
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

score_text=font.render(f"Hola: {score}", 0 , RED)   
text_lose = font.render(f'Adios: {lost}', 0, (RED))

player = Player('hero.png', 5, SCREEN_HEIGHT - 80, 5)
jose = Enemy('boss.png', SCREEN_WIDTH - 80, 200, 5)
Powerups = GameSprite('pac.png', SCREEN_WIDTH - 85, SCREEN_HEIGHT - 100, 0)
img_bullet = "bullet.png"

background = image.load('space.jpeg')
transform.scale(background, (1000, 800))

monsters=sprite.Group()
for i in range(1, 6):
    monster = Minion('enemy.png', randint(50,SCREEN_WIDTH-50), randint(10,80),randint(5,10))
    monsters.add(monster)


bullets = sprite.Group()

clock = time.Clock()

finish = False

run = True
while run:

    time.delay(10)

    clock.tick(144)

    for e in event.get():

        if e.type == QUIT:
            run = False

        elif  e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire() # Implementar el metodo fire()


    if not finish:
        window.fill((255, 255, 255))

        window.blit(background, (0, 0))
        window.blit(score_text, (10, 20)) 
        window.blit(text_lose, (10, 50))

        player.update()
        jose.update()
        monsters.update()

        player.reset()
        jose.reset()

        monsters.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(monsters,bullets,True,True)

        for c in collides:
            score += 1
            monster = Minion('enemy.png', randint(50,SCREEN_WIDTH-50), randint(10,80),randint(5,20))
            monsters.add(monster)


        if sprite.spritecollide(player, monsters, False) or lost >= max_lost:
            finish = True

            img = image.load('game-over_1.png')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (SCREEN_HEIGHT * d, SCREEN_HEIGHT)), (90, 0))

        if score >= goal:
            finish = True
            img = image.load('thumb.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

    display.update()