from pygame import *
from random import randint

# Inicializa todos los módulos de pygame (sonido, fuentes, gráficos, etc.)
init()

# --- Constantes y Configuración ---
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE = (255, 255, 255)
# Colores para textos de ganar/perder
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Nombres de archivos (Asegúrate de tener estos archivos en la misma carpeta)
BACKGROUND_MUSIC = 'space.ogg'
SHOOT_FX = 'fire.ogg'
BACKGROUND_IMG = 'galaxy.jpg'
PLAYER_IMG = 'rocket.png'
ENEMY_IMG = 'ufo.png'
BULLET_IMG = 'bullet.png'

FPS = 60

# Configuración de la Ventana Principal
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Project Shooter Python - Corrección')

# Cargar y escalar el fondo para que cubra toda la ventana
background = transform.scale(image.load(BACKGROUND_IMG), (SCREEN_WIDTH, SCREEN_HEIGHT))

# --- Sistema de Música y Sonido ---
mixer.init()
mixer.music.load(BACKGROUND_MUSIC)
mixer.music.play(-1) # El -1 hace que la música se repita en bucle infinito
fire_sound = mixer.Sound(SHOOT_FX)

# --- Fuentes y Textos ---
font.init()
font_ui = font.Font(None, 40)       # Fuente para puntuación
font_big = font.Font(None, 80)      # Fuente para Ganaste/Perdiste

# Variables de estado del juego
score = 0       # Enemigos eliminados
lost = 0        # Enemigos que se escaparon
goal = 10       # Meta para ganar (cambiado a 10 para probar más rápido, antes 20)
max_lost = 3    # Límite de enemigos perdidos para perder el juego (antes 5)

# --- Clases ---

class GameSprite(sprite.Sprite):
    """
    Clase padre para todos los objetos del juego (Jugador, Enemigos, Balas).
    Maneja la carga de imágenes, posición y dibujado básico.
    """
    def __init__(self, sprite_image, x_pos, y_pos, width, height, speed=0) -> None:
        super().__init__()
        self.width = width
        self.height = height
        # Cargar y escalar la imagen al tamaño deseado
        self.image = transform.scale(image.load(sprite_image), (width, height))
        # Obtener el rectángulo (hitbox) de la imagen para posicionamiento y colisiones
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed

    def reset(self):
        """Dibuja el sprite en la ventana en su posición actual"""
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    """Clase para la nave del usuario."""
    def update(self):
        """Maneja el movimiento con las teclas de flecha."""
        keys = key.get_pressed()

        # Mover a la izquierda si no se sale de la pantalla (> 5)
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        
        # Mover a la derecha considerando el ancho de la nave
        # (SCREEN_WIDTH - ancho_nave)
        elif keys[K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed
            
    def fire(self):
        """Crea una bala y la añade al grupo de sprites."""
        # Calculamos el centro X para que la bala salga de la punta de la nave
        # centerx de la nave - mitad del ancho de la bala
        bullet_x = self.rect.centerx - (15 // 2)
        bullet_y = self.rect.top # Sale desde la parte superior de la nave
        
        bullet = Bullet(BULLET_IMG, bullet_x, bullet_y, 15, 20, 15)
        bullets.add(bullet)
        fire_sound.play()

class Enemy(GameSprite):
    """Clase para los enemigos."""
    def update(self):
        """
        Mueve al enemigo hacia abajo.
        Si toca el borde inferior, cuenta como 'perdido' y reaparece arriba.
        """
        self.rect.y += self.speed
        global lost
        
        # Si el enemigo desaparece por abajo de la pantalla
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = randint(0, SCREEN_WIDTH - self.width)
            self.rect.y = 0
            # Aumentamos el contador de enemigos perdidos
            lost += 1 

class Bullet(GameSprite):
    """Clase para los proyectiles."""
    def update(self):
        """Mueve la bala hacia arriba y la elimina si sale de la pantalla."""
        self.rect.y -= self.speed
        
        # Si la bala sale de la pantalla (y < 0), la eliminamos de la memoria
        if self.rect.y < 0:
            self.kill()

# --- Creación de Objetos ---

# Crear Jugador: centrado horizontalmente, pegado abajo
player = Player(PLAYER_IMG, (SCREEN_WIDTH - 65) // 2, SCREEN_HEIGHT - 80, 65, 65, 5)

# Crear Grupo de Enemigos
monsters = sprite.Group()
for i in range(5):
    # Aparecen en X aleatoria, Y=0 (arriba), velocidad aleatoria
    enemy = Enemy(ENEMY_IMG, randint(0, SCREEN_WIDTH - 80), 0, 80, 50, randint(1, 3))
    monsters.add(enemy)

# Crear Grupo de Balas
bullets = sprite.Group()

# --- Bucle Principal del Juego ---
run = True
finish = False
clock = time.Clock()

while run:
    # 1. Manejo de Eventos (Cerrar ventana, teclas)
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        elif e.type == KEYDOWN:
            # Disparar solo si el juego no ha terminado
            if e.key == K_SPACE:
                if not finish:
                    player.fire()
                else: 
                    # Opcional: Reiniciar si se presiona espacio al terminar (no implementado logicamente reset)
                    pass

    # 2. Lógica y Renderizado (Si el juego está activo)
    if not finish:
        # Dibujar fondo
        window.blit(background, (0, 0))

        # Actualizar movimiento de sprites
        player.update()
        monsters.update()
        bullets.update()

        # Dibujar sprites
        player.reset()
        monsters.draw(window) # .draw es más eficiente para grupos que hacer un bucle manual
        bullets.draw(window)

        # --- Lógica de Colisiones ---
        
        # A) Colisión Bala vs Enemigo
        # groupcollide devuelve un diccionario de colisiones. 
        # (Grupo1, Grupo2, Kill1, Kill2) -> True significa eliminar el objeto
        collides = sprite.groupcollide(monsters, bullets, True, True)
        
        for c in collides:
            # Por cada colisión, sumamos puntos y creamos un nuevo enemigo
            score += 1
            enemy = Enemy(ENEMY_IMG, randint(0, SCREEN_WIDTH - 80), 0, 80, 50, randint(1, 3))
            monsters.add(enemy)

        # B) Colisión Jugador vs Enemigo (Game Over)
        # spritecollide(sprite, group, dokill)
        if sprite.spritecollide(player, monsters, False) or lost >= max_lost:
            finish = True
            # Mostrar mensaje de derrota
            lose_text = font_big.render('YOU LOSE!', True, RED)
            window.blit(lose_text, (200, 200))

        # C) Condición de Victoria
        if score >= goal:
            finish = True
            # Mostrar mensaje de victoria
            win_text = font_big.render('YOU WIN!', True, GREEN)
            window.blit(win_text, (200, 200))

        # --- Interfaz de Usuario (UI) ---
        text_score = font_ui.render(f'Score: {score}', 1, WHITE)
        window.blit(text_score, (10, 20))

        text_lost = font_ui.render(f'Missed: {lost}', 1, WHITE)
        window.blit(text_lost, (10, 50))

    else:
        # El juego terminó (finish = True), pero seguimos actualizando la pantalla
        # para que se vean los mensajes de Win/Lose.
        # Aquí no hacemos update() ni movemos nada.
        pass

    # Actualizar la pantalla completa y mantener los FPS
    display.update()
    clock.tick(FPS)

quit()
