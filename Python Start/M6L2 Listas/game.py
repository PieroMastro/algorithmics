import pygame
from random import randint

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
background = (233, 242, 242)
question_color = (40, 222, 88)
answer_color = (58, 152, 240)


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Preguntas y Respuestas')

class TextArea():
    def __init__(self, x_pos=0, y_pos=0, width=80, height=20, color=None):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.color = color
        self.titles = [] # creando una lista vacia para almacenar las preguntas/respuestas

    # metodo que agrega preguntas/respuestas a la lista
    def add_text(self, text):
        self.titles.append(text)

    # modificamos el metodo para seleccionar el texto segun su posicion en la lista
    def set_text(self, element=0, font_size=12, text_color=BLACK):
        self.text = self.titles[element]
        self.image = pygame.font.Font(None, font_size).render(self.text, True, text_color)

    def draw_card(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# creamos una instancia para preguntas
question = TextArea(100, 100, 600, 150, question_color)
# rellenamos la lista con elementos
question.add_text('Pregunta')
question.add_text('¿Qué estudias en Algorithmics?')
question.add_text('¿Qué idioma se habla en Francia?')
question.add_text('¿Qué crece en un manzano?')
question.add_text('¿Qué cae del cielo cuando llueve?')
question.add_text('¿Qué van a comer para la cena?')
question.add_text('Cuál es el planeta más grande?')
question.add_text('Cuántos continentes hay en el mundo?')
question.add_text('Colores de la bandera de Japon')
# colocamos la primera pregunta (indice 0)
question.set_text(0, 75)
# dibujamos en pantalla
question.draw_card(10, 30)

# repetimos para respuestas
answer = TextArea(100, 350, 600, 150, answer_color)
answer.add_text('Respuesta')
answer.add_text('Python')
answer.add_text('Francés')
answer.add_text('Manzanas')
answer.add_text('Gotas de lluvia')
answer.add_text('Un asado con champiñones')
answer.add_text('Júpiter')
answer.add_text('5, 6 o 7')
answer.add_text('Blanco y Rojo')
answer.set_text(0,75)
answer.draw_card(10, 30)


clock = pygame.time.Clock()
run = True

while run:

    window.fill(background)
    question.draw_card(10, 50)
    answer.draw_card(10, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                # random num para seleccionar el elemento de la lista
                num = randint(1, len(question.titles) - 1)
                # establecemos el nuevo elemento segun el lugar que ocupa en nuestra lista
                question.set_text(num, 40)
                # actualizamos el contenido de nuestro objeto
                question.draw_card(10, 50)
            
            if event.key == pygame.K_a:
                num = randint(1, len(answer.titles) - 1)
                answer.set_text(num, 40)
                answer.draw_card(10, 50)

    
    pygame.display.update()
    clock.tick(40)

pygame.quit()