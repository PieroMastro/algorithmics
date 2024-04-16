from pygame import *

init()

#crear ventana de juego
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
blue_x, blue_y = 100, 400
pink_x, pink_y = 600, 400
speed = 10

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Catch Up!')

#establecer fondo de la escena
background = image.load('background.png')
background_img = transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#crear 2 objetos y colocarlos en la escena
blue = transform.scale(image.load('sprite1.png'), (100, 100))
pink = transform.scale(image.load('sprite2.png'), (100, 100))
pink = transform.flip(pink, True, False)

running = True
clock = time.Clock()

while running:
#manejo de evento “clic en “Cerrar ventana”
    for e in event.get():
        if e.type == QUIT:
            running = False    

    window.blit(background_img, (0, 0))
    window.blit(blue, (blue_x, blue_y))
    window.blit(pink, (pink_x, pink_y))

    keys = key.get_pressed()
    #movimiento sprite "blue"
    if keys[K_a] and blue_x > 5:
        blue_x -= speed
    if keys[K_d] and blue_x < SCREEN_WIDTH - 105:
        blue_x += speed
    if keys[K_w] and blue_y > 5:
        blue_y -= speed
    if keys[K_s] and blue_y < SCREEN_HEIGHT - 105:
        blue_y += speed
        
    #movimiento sprite "pink"
    if keys[K_LEFT] and pink_x > 5:
        pink_x -= speed
    if keys[K_RIGHT] and pink_x < SCREEN_WIDTH - 105:
        pink_x += speed
    if keys[K_UP] and pink_y > 5:
        pink_y -= speed
    if keys[K_DOWN] and pink_y < SCREEN_HEIGHT - 105:
        pink_y += speed

    display.update()
    clock.tick(60)

quit()
