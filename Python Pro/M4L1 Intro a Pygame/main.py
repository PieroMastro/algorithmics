from pygame import *

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

init()

window = display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
display.set_caption('Demo')

run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update
quit()
