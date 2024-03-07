import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision")

#create main rectangle & obstacle rectangle
rect_1 = pygame.Rect(0, 0, 25, 25)
obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)

#define color
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#hide mouse cursor
pygame.mouse.set_visible(False)

run = True
while run:
    #update background
    screen.fill(BG)

    #check collision and change color
    color = GREEN
    if rect_1.colliderect(obstacle_rect):
        color = RED

    #get mouse coordinates and use them to position the rectangle
    position = pygame.mouse.get_pos()
    rect_1.center = position

    #draw both rectangles
    pygame.draw.rect(screen, color, rect_1)
    pygame.draw.rect(screen, BLUE, obstacle_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.flip()

pygame.quit()