# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  VERSION 2.0                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importando librerias (os no es requerida)
from pygame import *
from random import randint
import os

# cargando funciones para trabajar por separado con las fuentes
font.init()
# durante el juego escribimos etiquetas de tamaño 36 y estilo 'bold'
font = font.Font(None, 36, bold= True)

# definiendo constantes:
SCREN_WIDTH, SCREN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
VICTORY_IMG = "thumb.jpg" # fondo de victoria
LOST_IMG = "game_over.png" # fondo de derrota
BACKGROUND = "galaxy.jpg" # fondo de juego
BULLET_IMG = os.path.join("images", "bullet.png")
EXPLOSION_IMG = os.path.join("images", 'explosion.gif') # explosion
HERO_IMG = "rocket.png" # personaje
ENEMY_IMG = "ufo.png" # enemigo
FPS = 60
score = 0 # registro de disparos acertados 
goal = 20 # cuántos enemigos necesitan ser eliminados para ganar
lost = 0 # enemigos que cruzan el final del area establecida
max_lost = 3 # el jugador pierde si falla tantos disparos (se establecen 3)

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, sprite_img, x_pos, y_pos, width, height, sprite_speed):
        # llamando al constructor de clase (Sprite)
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(sprite_img), (width, height))
        self.speed = sprite_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrita
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# clase de jugador principal
class Player(GameSprite):
    # método para controlar el objeto con las flechas del teclado
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < SCREN_WIDTH - 80:
            self.rect.x += self.speed
    # el método 'fire' (usamos la posición del jugador para crear una bala)
    def fire(self):
        bullet = Bullet(BULLET_IMG, self.rect.centerx, self.rect.top, randint(10, 30), 20, -15)
        bullets.add(bullet)

# clase del objeto enemigo   
class Enemy(GameSprite):
    # movimiento del enemigo
    def update(self):
        self.rect.y += self.speed
        global lost # definiendo una variable global (no limitada al scope de la funcion)
        # desaparece si alcanza el borde de la pantalla
        if self.rect.y > SCREN_HEIGHT:
            self.rect.x = randint(80, SCREN_WIDTH - 80)
            self.rect.y = 0
            lost = lost + 1

# clase del objeto de la bala   
class Bullet(GameSprite):
    # movimiento del enemigo
    def update(self):
        self.rect.y += self.speed
        # desaparece si alcanza el borde de la pantalla
        if self.rect.y < 0:
            self.kill()


# Creando una ventana
window = display.set_mode((SCREN_WIDTH, SCREN_HEIGHT))
display.set_caption("Shooter")
background = transform.scale(image.load(BACKGROUND), (SCREN_WIDTH, SCREN_HEIGHT))
explosion_img = transform.scale(image.load(EXPLOSION_IMG), (50, 50))

# creando objetos
ship = Player(HERO_IMG, 5, SCREN_HEIGHT - 100, 80, 100, 10)

# creando un grupo de objetos enemigos
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(ENEMY_IMG, randint(80, SCREN_WIDTH - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

# creando un grupo de objetos de balas
bullets = sprite.Group()

# variable para establecer FPS
clock = time.Clock()

# la variable “juego terminado”: apenas sea True, los objetos dejan de funcionar en el ciclo principal
finish = False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Implementing restart game function                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def restart_game():
    global score, lost, monsters, bullets, ship, finish
    score = 0
    lost = 0
    monsters.empty()
    bullets.empty()
    ship.rect.x = 5
    ship.rect.y = SCREN_HEIGHT - 100
    finish = False

    # Create new enemy objects and add them to the monsters group
    for i in range(1, 6):
        monster = Enemy(ENEMY_IMG, randint(80, SCREN_WIDTH - 80), -40, 80, 50, randint(1, 5))
        monsters.add(monster)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Implementing restart game function                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Ciclo de juego principal:
run = True # El ciclo principal se termina al presionar el botón de cerrar ventana
while run:
    # Implementamos un ciclo para recorre todos los eventos posibles.
    for e in event.get():
        # si se registra el evento de botón cerrar ("X")
        if e.type == QUIT:
            run = False
        # si se registra el evento de barra espaciadora – el objeto dispara
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
    
    # el juego: acciones del objeto, comprobación de las reglas del juego, redibujando
    if not finish:
        # actualizando el fondo
        window.blit(background,(0,0))

        # escribiendo texto en la pantalla
        text = font.render(f'Score: {score}', 0, (WHITE))
        window.blit(text, (10, 20))

        text_lose = font.render(f'Enemies lost: {lost}', 1, (RED))
        window.blit(text_lose, (10, 50))


        # creando movimiento del objeto
        ship.update()
        monsters.update()
        bullets.update()


        # actualizándolos en nuevas ubicaciones con cada iteración del ciclo
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)


        # comprobación de colisión de bala-monstruo (tanto el monstruo como la bala desaparecen al tocarse)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        
        for c in collides:
            # Mostrar la explosión en la posición del enemigo colisionado
            window.blit(explosion_img, c.rect.topleft) 

            # Actualizar la pantalla para mostrar la explosión
            display.update()

            # Esperar un breve período de tiempo para que la explosión sea visible
            time.delay(40)  # Ajusta este valor según sea necesario

            # Eliminar la explosión al rellenar el área con el fondo
            window.blit(background, (0, 0))

            # este ciclo se repetirá tantas veces como los monstruos que sean matados
            score = score + 1
            monster = Enemy(ENEMY_IMG, randint(80, SCREN_WIDTH - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        # posible derrota: muchos fallos o el personaje chocó con el enemigo
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True # es una derrota, establecemos el fondo y ya no podemos controlar los objetos.
            # calculando la tasa
            explo = image.load(EXPLOSION_IMG)
            window.blit(explo, (-200, 0))
            display.update()
            time.delay(200)
            img = image.load(LOST_IMG)
            d = img.get_width() // img.get_height()
            window.fill((219, 199, 22))
            window.blit(transform.scale(img, (SCREN_HEIGHT * d, SCREN_HEIGHT)), (90, 0))
    
        # comprobación de victoria: ¿cuántos puntos se obtuvieron?
        if score >= goal:
            finish = True
            img = image.load(VICTORY_IMG)
            window.fill(WHITE)
            window.blit(transform.scale(img, (SCREN_WIDTH, SCREN_HEIGHT)), (0, 0))

    display.update()
        
    # se refrescan las imagenes a 60 FPS
    clock.tick(FPS)