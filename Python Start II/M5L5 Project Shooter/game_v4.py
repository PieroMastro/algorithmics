
from pygame import *
from random import randint

init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
CYAN = (0, 255, 255)
BACKGROUND_MUSIC = 'space.ogg'
SHOOT_FX = 'fire.ogg'
BACKGROUND_IMG = 'galaxy.jpg'
PLAYER_IMG = 'rocket.png'
ENEMY_IMG = 'ufo.png'
BULLET_IMG = 'bullet.png'
MUSIC = 'space.ogg'
FPS = 60

# Main Window
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Project Shooter Python Start II')
background = transform.scale(image.load(BACKGROUND_IMG), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Game Music
mixer.init()
mixer.music.load(BACKGROUND_MUSIC)
mixer.music.play()

fire_sound = mixer.Sound(SHOOT_FX)

# Game functionality
font.init()
font = font.Font(None, 40)
score = 0
win_score = 10
lost = 0

# Main Class
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x_pos, y_pos, width, height, speed= 0) -> None:
        super().__init__()

        self.width = width
        self.height = height
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
        bullet = Bullet(BULLET_IMG, self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)
        fire_sound.play()
        print('Pew Pew!')


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = randint(0, SCREEN_WIDTH - self.width)
            self.speed = randint(1, 4)
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.y <= 0:
            self.kill()


# Objects
player = Player(PLAYER_IMG, (SCREEN_WIDTH - 65) // 2, SCREEN_HEIGHT - 80, 65,65, 5)

monsters = sprite.Group()
for enemy in range(5):
    enemy = Enemy(ENEMY_IMG, randint(0, SCREEN_WIDTH - 80), 0, 80, 50, randint(1, 4))
    monsters.add(enemy)

bullets = sprite.Group()

# Main Game
run = True
finish = False
clock = time.Clock()

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
            
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if not finish:
        window.blit(background, (0, 0))
        score_text = font.render(f'Score: {score}', 1, WHITE)
        lost_text = font.render(f'Lost: {lost}', 1, WHITE)
        window.blit(score_text, (20, 20))
        window.blit(lost_text, (20, 60))

        player.reset()
        player.update()

        bullets.draw(window)
        bullets.update()

        monsters.draw(window)
        monsters.update()
        
        collisions = sprite.groupcollide(monsters, bullets, True, True)
        
        for collision in collisions:
            score += 1
            enemy = Enemy(ENEMY_IMG, randint(0, SCREEN_WIDTH - 80), 0, 80, 50, randint(1, 4))
            monsters.add(enemy)

        if lost == 5 or sprite.spritecollide(player, monsters, False):
            finish = True
            window.fill(BLACK)
            mixer.music.stop()
            game_over = font.render('GAME OVER', 1, RED)
            window.blit(game_over, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            
        if score == win_score:
            finish = True
            window.fill(BLACK)
            mixer.music.stop()
            you_win = font.render('VICTORY', 1, CYAN)
            window.blit(you_win, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))


    display.update()
    clock.tick(FPS)

quit()