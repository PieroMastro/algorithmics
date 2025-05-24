import pygame
pygame.init()

SW, SH = 500, 500
BACK_COLOR = (200, 255, 255)

screen = pygame.display.set_mode((SW, SW))
pygame.display.set_caption('Arkanoid')

class Area():
    def __init__(self, x, y, width, height, color=None):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def change_color(self, new_color):
        self.color = new_color

    def fill(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Picture(Area):
    def __init__(self, img, x, y, width, height):
        super().__init__(x, y, width, height, color=None)
        self.image = pygame.image.load(img)

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

platform_x, platform_y = 200, 300
platform = Picture('platform.png', platform_x, platform_y, 100, 30)
ball = Picture('ball.png', platform_x, platform_y - 60, 50, 50)

monsters = []
rows = 3
enemies_per_row = 9
size = 50
distance = 5
start_y = 5
start_x = [5, 33, 60]

for i in range(rows):
    row_start_x = start_x[i]
    y = start_y + (i * (size + distance))
    x = row_start_x

    for j in range(enemies_per_row):
        enemy = Picture('enemy.png', x, y, size, size)
        monsters.append(enemy)
        x += (size + distance)
    enemies_per_row -= 1


run = True
clock = pygame.time.Clock()
screen.fill(BACK_COLOR)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    platform.render()
    ball.render()
    for monster in monsters:
        monster.render()

    pygame.display.update()
    clock.tick(40)

pygame.quit()
