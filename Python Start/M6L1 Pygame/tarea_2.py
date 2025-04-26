import pygame
from random import randint

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
BACK_COLOR = (233, 242, 242)
question_color = (40, 222, 88)
answer_color = (58, 152, 240)


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Preguntas y Respuestas')

class TextArea():
    def __init__(self, x_pos, y_pos, width, height, color=None):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.color = color

    def set_text(self, text, font_size=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, font_size).render(text, True, text_color)

    def draw_card(self, shift_x=10, shift_y=10):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

question = TextArea(100, 100, 600, 150, question_color)
question.set_text('Pregunta', 50, BLACK)

answer = TextArea(100, 350, 600, 150, answer_color)
answer.set_text('Respuesta', 50, BLACK)


clock = pygame.time.Clock()
run = True

while run:

    window.fill(BACK_COLOR)
    question.draw_card(10, 50)
    answer.draw_card(10, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                num = randint(1, 3)
                if num == 1:
                    question.set_text('Cuál es el planeta más grande?', 40)
                elif num == 2:
                    question.set_text('Cuántos continentes hay en el mundo?', 40)
                elif num == 3:
                    question.set_text('Colores de la bandera de Japon', 40)

                question.draw_card(10,50)
            
            if event.key == pygame.K_a:
                num = randint(1, 3)
                if num == 1:
                    answer.set_text('Júpiter', 40)
                elif num == 2:
                    answer.set_text('5, 6 o 7', 40)
                elif num == 3:
                    answer.set_text('Blanco y Rojo', 40)

                answer.draw_card(10,50)

    
    pygame.display.update()
    clock.tick(40)

pygame.quit()
