import pygame

pygame.init()

# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
BACKGROUND = (120, 238, 247)

# Definiendo clases
# class Area():
    # def __init__(self, x_pos=0, y_pos=0, width=10, height=10, color=None):
        # self.rect = pygame.Rect(x_pos, y_pos, width, height)
        # self.rect.x = x_pos
        # self.rect.y = y_pos
        # self.fill_color = color

    # def color(self, new_color):
        # self.fill_color = new_color

    # def fill(self):
        # pygame.draw.rect(screen, self.fill_color, self.rect)

    # def outline(self, frame_color, thickness):
        # pygame.draw.rect(screen, frame_color, self.rect, thickness)

# class Picture(Area):
    # def __init__(self, sprite_img, x_pos=0, y_pos=0, width=10, height=10):
        # Area.__init__(self, x_pos=x_pos, y_pos=y_pos, width=width, height=height, color=None)
        # self.image = pygame.image.load(sprite_img)

    # def draw(self):
        # screen.blit(self.image, (self.rect.x, self.rect.y))


class GameSprite():
    def __init__(self, sprite_image, x_pos, y_pos, width, height):
        self.image = pygame.transform.scale(pygame.image.load(sprite_image), (50, 50))
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x_pos, y_pos):
        return self.rect.collidepoint(x_pos, y_pos)



# Main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Arkanoid')

# Creando instancias de objetos
player = GameSprite('mario.png', 160, 200, 50, 50)
paddle = GameSprite('warp_pipe.png', 160, 250, 50, 50)

# Creacion de enemigos
enemy_x, enemy_y = 5, 5
count = 9
monsters = []

for i in range(3):
    y = (55 * i) + enemy_y
    x = (27.5 *i) + enemy_x

    for enemy in range(count):
        enemy = GameSprite('goomba.png', x, y, 50, 50)
        monsters.append(enemy)
        x += 55
    count -= 1
        
# Game Loop
clock = pygame.time.Clock()
running = True
finish = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not finish:
        screen.fill(BACKGROUND)
        player.draw()           
        paddle.draw()

        for monster in monsters:
            monster.draw()
            
    pygame.display.update()
    clock.tick(40)

pygame.quit()

