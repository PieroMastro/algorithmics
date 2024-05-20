import pygame
from random import randint
import time

# Inicializando la libreria y cargando recursos
pygame.init()


# Colores 
BACKGROUND = (200, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
BLACK = (0, 0, 0)

# Creando la ventana principal
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(BACKGROUND)

# Obhjeto clock para frame control
clock = pygame.time.Clock()


# Clase para representar objetos rectangulares
class Area():
    def __init__(self, x_pos=0, y_pos=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x_pos, y_pos, width, height) #rectángulo
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness): #delimita un rectángulo existente
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x_pos, y_pos):
        return self.rect.collidepoint(x_pos, y_pos)  


# Clase derivada Label()
class Label(Area):
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Creando multiples objetos
cards = []
num_cards = 4
x_pos = 70

for i in range(num_cards):
    new_card = Label(x_pos, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x_pos += 100 #x_pos = x_pos + 100


# Estableciendo el tiempo espera para renderizar texto
wait = 0

# Game Loop
while True:
    # Colocando todas las cartas (objetos) en pantalla
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if (i + 1) == click:
                cards[i].draw(10,40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    # Captura y procesamiento del evento "click"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                # Buscando la tarjeta que toco el click
                if cards[i].collidepoint(x, y):
                    # Si hay etiqueta en la tarjeta la coloreamos verde
                    if (i + 1) == click:
                        cards[i].color(GREEN)
                    # Caso contrario coloreamos rojo
                    else:
                        cards[i].color(RED)

                    cards[i].fill()

    pygame.display.update()
    clock.tick(40)

# Saliendo de pygame y removiendo los recursos
pygame.quit()  