from pygame import *
from random import randint
import os

# cargando funciones para trabajar por separado con las fuentes
font.init()
# durante el juego escribimos etiquetas de tamaño 36
font = font.Font(None, 36, bold= True)

# necesitamos estas imágenes:
img_win = "thumb.jpg" # fondo de victoria
img_los = "game_over.png" # fondo de derrota
img_back = "galaxy.jpg" # fondo de juego

img_bullet = os.path.join("images", "bullet.png") # bala
img_hero = "rocket.png" # personaje
img_enemy = "ufo.png" # enemigo

score = 0 # registro de disparos acertados 
goal = 10 # cuántos enemigos necesitan ser eliminados para ganar
lost = 0 # enemigos que cruzan el final del area establecida
max_lost = 3 # el jugador pierde si falla tantos disparos (se establecen 3)


# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamando al constructor de clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrita
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

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
    # el método “disparo” (usamos la posición del jugador para crear una bala)
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

# clase del objeto enemigo   
class Enemy(GameSprite):
    # movimiento del enemigo
    def update(self):
        self.rect.y += self.speed
        global lost
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
SCREN_WIDTH = 800
SCREN_HEIGHT = 600
window = display.set_mode((SCREN_WIDTH, SCREN_HEIGHT))
display.set_caption("Shooter")
background = transform.scale(image.load(img_back), (SCREN_WIDTH, SCREN_HEIGHT))

# constantes:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# creando objetos
ship = Player(img_hero, 5, SCREN_HEIGHT - 100, 80, 100, 10)


# creando un grupo de objetos enemigos
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, SCREN_WIDTH - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

# creando un grupo de objetos de balas
bullets = sprite.Group()

# variable para establecer FPS
clock = time.Clock()

# la variable “juego terminado”: apenas sea True, los objetos dejan de funcionar en el ciclo principal
finish = False

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
        text = font.render(f'Score: {score}', 1, (WHITE))
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
            # este ciclo se repetirá tantas veces como los monstruos que sean matados
            score = score + 1
            monster = Enemy(img_enemy, randint(80, SCREN_WIDTH - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)


        # posible derrota: muchos fallos o el personaje chocó con el enemigo
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True # es una derrota, establecemos el fondo y ya no podemos controlar los objetos.
            # calculando la tasa
            img = image.load(img_los)
            d = img.get_width() // img.get_height()
            window.fill((219, 199, 22))
            window.blit(transform.scale(img, (SCREN_HEIGHT * d, SCREN_HEIGHT)), (90, 0))
    
        # comprobación de victoria: ¿cuántos puntos se obtuvieron?
        if score >= goal:
            finish = True
            img = image.load(img_win)
            window.fill(WHITE)
            window.blit(transform.scale(img, (SCREN_WIDTH, SCREN_HEIGHT)), (0, 0))


        display.update()
        
    # el ciclo se ejecuta cada 0.05 segundos
    time.delay(20)
    # se refrescan las imagenes a 60 FPS
    clock.tick(60)