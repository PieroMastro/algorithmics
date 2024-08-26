from pygame import *

init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SQUARE_COLOR = (0, 255, 255)
BACKGROUND_IMG = ('jungle.png')
PLAYER_IMG = '1-2.png'

x, y = 100, 100

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Intro to Pygame')

BACKGROUND = image.load(BACKGROUND_IMG)
BACKGROUND = transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = transform.scale(image.load(PLAYER_IMG), (60, 60))
square = Rect(x, y, 40, 60)


clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_d:
                square.x += 5

    keys = key.get_pressed()
    if keys[K_s] and square.y <= SCREEN_HEIGHT - 60:
        square.y += 5
    elif keys[K_w] and square.y > 0:
        square.y -= 5


    screen.fill(BLACK)
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(player, (100, 450))
    draw.rect(screen, SQUARE_COLOR, square )

    display.update()
    clock.tick(60)

quit()

