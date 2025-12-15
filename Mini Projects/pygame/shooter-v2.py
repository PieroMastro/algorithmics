from pygame import *
from random import randint
from time import time as timer # Importamos 'time' como 'timer' para evitar conflictos de nombres

# Inicializa todos los módulos de pygame
init()

# --- Constantes y Configuración ---
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
YELLOW = (252, 186, 3)

# Archivos de recursos
BACKGROUND_MUSIC = 'space.ogg'
SHOOT_FX = 'fire.ogg'
BACKGROUND_IMG = 'galaxy.jpg'
PLAYER_IMG = 'rocket.png'
ENEMY_IMG = 'ufo.png'
ASTEROID_IMG = 'asteroid.png' # Nueva imagen para asteroides
BULLET_IMG = 'bullet.png'

FPS = 60

# --- Fuentes y Textos ---
font.init()

# Fuente grande para mensajes de fin de juego
font_big = font.SysFont('Arial', 80)
txt_win = font_big.render('VICTORY', True, GREEN)
txt_lose = font_big.render('GAME OVER', True, RED)

# Fuente normal para la interfaz (puntuación, recarga)
font_ui = font.SysFont('Arial', 40)

# --- Ventana Principal ---
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Project Shooter Python Start II')
# Escalar el fondo para que cubra toda la ventana
background = transform.scale(image.load(BACKGROUND_IMG), (SCREEN_WIDTH, SCREEN_HEIGHT))

# --- Sonido y Música ---
mixer.init()
mixer.music.load(BACKGROUND_MUSIC)
mixer.music.play(-1) # -1 para bucle infinito
fire_sound = mixer.Sound(SHOOT_FX)

# --- Variables de Estado del Juego ---
score = 0           # Enemigos destruidos
goal = 20           # Meta para ganar
lost = 0            # Enemigos que se escaparon
max_lost = 5        # Límite de enemigos perdidos antes de perder
bullets_fired = 0   # Contador de balas disparadas (para la mecánica de recarga)
is_reloading = False # Estado de recarga
last_reload_time = 0 # Momento en que inició la recarga

# --- Clases ---

class GameSprite(sprite.Sprite):
    """
    Clase padre para todos los objetos visuales del juego.
    Maneja la carga de imagen, posición (rect) y velocidad.
    """
    def __init__(self, sprite_image, x_pos, y_pos, width, height, speed=0) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed

    def reset(self):
        """Dibuja el sprite en la pantalla"""
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    """Clase del jugador (la nave)."""
    def update(self):
        """Maneja el movimiento con el teclado."""
        keys = key.get_pressed()
        
        # Movimiento izquierda (con límite de pantalla)
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        
        # Movimiento derecha (con límite de pantalla)
        elif keys[K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed
            
    def fire(self):
        """Dispara una bala."""
        # La bala sale del centro superior de la nave
        bullet = Bullet(BULLET_IMG, self.rect.centerx - 7, self.rect.top, 15, 20, 15)
        bullets.add(bullet)
        fire_sound.play()

class Enemy(GameSprite):
    """Clase para los enemigos (UFOs)."""
    def update(self):
        """
        Mueve al enemigo hacia abajo.
        Si sale de la pantalla, cuenta como 'perdido' y reaparece arriba.
        """
        self.rect.y += self.speed
        global lost
        
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = randint(0, SCREEN_WIDTH - self.width)
            self.rect.y = 0
            self.speed = randint(1, 3) # Velocidad aleatoria nueva
            lost += 1

class Asteroid(GameSprite):
    """
    Clase para los asteroides (Nueva mecánica).
    Se mueven igual que los enemigos pero NO suman 'lost' si salen de la pantalla.
    Son obstáculos puros.
    """
    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = randint(0, SCREEN_WIDTH - self.width)
            self.rect.y = -40 # Reaparecen un poco más arriba
            self.speed = randint(1, 5) # Velocidad variable

class Bullet(GameSprite):
    """Clase para los proyectiles."""
    def update(self):
        """Mueve la bala hacia arriba y la elimina si sale de la pantalla."""
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# --- Creación de Objetos ---

# Jugador
player = Player(PLAYER_IMG, (SCREEN_WIDTH - 65) // 2, SCREEN_HEIGHT - 80, 65, 65, 5)

# Grupo de Enemigos (UFOs)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy(ENEMY_IMG, randint(0, SCREEN_WIDTH - 80), -40, 80, 50, randint(1, 3))
    monsters.add(enemy)

# Grupo de Asteroides (Obstáculos)
asteroids = sprite.Group()
for i in range(3): # Creamos 3 asteroides
    asteroid = Asteroid(ASTEROID_IMG, randint(0, SCREEN_WIDTH - 80), -40, 80, 50, randint(1, 5))
    asteroids.add(asteroid)

# Grupo de Balas
bullets = sprite.Group()

# --- Bucle Principal del Juego ---
run = True
finish = False
clock = time.Clock()

while run:
    # 1. Manejo de Eventos
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                # Mecánica de Disparo y Recarga
                if not is_reloading and not finish: # Solo dispara si no está recargando y el juego sigue
                    if bullets_fired < 5:
                        player.fire()
                        bullets_fired += 1
                    
                    # Si llegamos a 5 balas, iniciamos la recarga
                    if bullets_fired >= 5:
                        is_reloading = True
                        last_reload_time = timer() # Guardamos el tiempo actual

    # 2. Lógica del Juego
    if not finish:
        # Dibujar fondo y textos de UI
        window.blit(background, (0, 0))
        
        text_score = font_ui.render(f'Score: {score}', 1, WHITE)
        window.blit(text_score, (10, 20))

        text_lost = font_ui.render(f'Missed: {lost}', 1, WHITE)
        window.blit(text_lost, (10, 60))

        # Actualizar y dibujar sprites
        player.update()
        player.reset()

        monsters.update()
        monsters.draw(window)
        
        asteroids.update()
        asteroids.draw(window)

        bullets.update()
        bullets.draw(window)

        # --- Mecánica de Recarga ---
        if is_reloading:
            now_time = timer()
            
            # Si han pasado menos de 3 segundos (tiempo de recarga)
            if now_time - last_reload_time < 3:
                reload_text = font_ui.render('RELOADING...', 1, YELLOW)
                window.blit(reload_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50))
            else:
                # Recarga terminada
                bullets_fired = 0
                is_reloading = False

        # --- Colisiones ---

        # A) Balas vs Enemigos (UFOs)
        # Elimina bala y enemigo. Suma puntos.
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            # Respawnear enemigo
            enemy = Enemy(ENEMY_IMG, randint(0, SCREEN_WIDTH - 80), -40, 80, 50, randint(1, 3))
            monsters.add(enemy)

        # B) Balas vs Asteroides
        # Nota: Normalmente las balas NO destruyen asteroides.
        # Aquí haremos que las balas se destruyan al chocar con asteroides, pero el asteroide sigue.
        sprite.groupcollide(asteroids, bullets, False, True) 

        # C) Jugador vs Enemigos O Jugador vs Asteroides (Game Over)
        if sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, asteroids, False):
            finish = True
            # Pantalla de Derrota
            # window.fill(BLACK) # Opcional: limpiar fondo
            window.blit(txt_lose, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

        # D) Límite de enemigos perdidos (Game Over)
        if lost >= max_lost:
            finish = True
            window.blit(txt_lose, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

        # E) Condición de Victoria
        if score >= goal:
            finish = True
            window.blit(txt_win, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))

    else:
        # El juego terminó, pero seguimos actualizando la pantalla para mostrar el mensaje final
        pass

    display.update()
    clock.tick(FPS)

quit()
