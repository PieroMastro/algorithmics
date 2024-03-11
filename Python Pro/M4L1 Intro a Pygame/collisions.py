from pygame import *
from random import randint

init()

# define constants for colors and screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# main window
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('My First Game')

# create main rectangle & obstacle rectangle
square = Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, 50)
obstacle = Rect(randint(0, 700), randint(0, 500), 50, 50)

finish = False

run = True
while run:
    # main event
    for e in event.get():
            
        if e.type == QUIT:
            run = False

    if not finish:
        # update screen
        window.fill(WHITE)

        # check collision and change color
        color = GREEN
        if square.colliderect(obstacle):
            color = RED
            finish = True
            window.fill(BLACK)
            game_over = image.load('game-over_2.png')
            window.blit(transform.scale(game_over, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

        # draw objets on screen
        draw.rect(window, BLUE, square) # surface, color, object (or params)
        draw.rect(window, color, obstacle)

        # get mouse coordinates and use them to position the rectangle
        position = mouse.get_pos()
        square.center = position

    display.update()

quit()
