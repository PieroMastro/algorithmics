import pygame

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

    def set_text(self, text, font_size=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, font_size).render(text, True, text_color)

    def draw_text_area(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

question = TextArea(100, 100, 600, 150, question_color)
question.set_text('Pregunta de prueba', 50, BLACK)

answer = TextArea(100, 350, 600, 150, answer_color)
answer.set_text('Respuesta de prueba', 50, BLACK)


clock = pygame.time.Clock()
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(background)
    question.draw_text_area(10, 10)
    answer.draw_text_area(10, 10)
    
    pygame.display.update()
    clock.tick(40)

pygame.quit()