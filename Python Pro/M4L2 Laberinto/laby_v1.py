from pygame import *

# Main Window:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Labyrinth Project')

image_hero = transform.scale(image.load('hero.png'), (80, 80))
speed_hero = 5
rect_hero = image_hero.get_rect()
rect.x_hero = 5
rect.y_hero = SCREEN_HEIGHT - 80

side = "izquierda"
image_enemy = transform.scale(image.load('cyborg.png'), (80, 80))
speed_enemy = 5
rect_enemy = image_enemy.get_rect()
rect.x_enemy = SCREEN_WIDTH - 80
rect.y_enemy = 200

wall_width = 300
wall_height = 10
wall_x = SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3
wall_y = SCREEN_HEIGHT / 2
 
image_final = transform.scale(image.load('pac.png'), (80, 80))
rect_final = image_final.get_rect()
rect.x_final = SCREEN_WIDTH - 85
rect.y_final = SCREEN_HEIGHT - 100

# Imagen de la pared – un rectángulo del tamaño y color deseado:
image_wall = Surface([wall_width, wall_height])
image_wall.fill((0, 0, 0))
rect_wall = image_wall.get_rect()
rect_wall = Rect(wall_x, wall_y, wall_width, wall_height)

# Variable responsable por cómo termina el juego:
finish = False

# Game Loop:
run = True
while run:
    time.delay(50)
    # Event Handler (comprobando todos los eventos que pueden suceder):
    for e in event.get():
        # Evento del clic del botón "cerrar"
        if e.type == QUIT:
            run = False

    # Comprobamos que el juego no está terminado todavía:
    if not finish:
        # Refrescamos nuestra ventana con cada iteración:
        window.fill((0, 0, 0))

        # Dibujar las paredes:
        draw.rect(window, (255, 255, 255), (wall_x, wall_y, wall_width, wall_height))
        # Ejecutar el movimiento del objeto:
        keys = key.get_pressed()
        if keys[K_LEFT] and rect.x_hero > 5:
            rect.x_hero -= speed_hero
        if keys[K_RIGHT] and rect.x_hero < SCREEN_WIDTH - 80:
            rect.x_hero += speed_hero
        if keys[K_UP] and rect.y_hero > 5:
            rect.y_hero -= speed_hero
        if keys[K_DOWN] and rect.y_hero < SCREEN_HEIGHT - 80:
            rect.y_hero += speed_hero
        
        
        if rect.x_enemy <= 410:
            side = "right"
        if rect.x_enemy >= SCREEN_WIDTH - 85:
            side = "left"
        if side == "left":
            rect.x_enemy -= speed_enemy
        else:
            rect.x_enemy += speed_enemy

        # Actualizarlos en una nueva ubicación con cada iteración del ciclo
        window.blit(image_hero, (rect.x_hero, rect.y_hero))
        window.blit(image_enemy, (rect.x_enemy, rect.y_enemy))
        window.blit(image_final, (rect.x_final, rect.y_final))

    display.update()
