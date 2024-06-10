import pygame

pygame.init()

# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
BACKGROUND = (120, 238, 247)
# Movimiento de nuestro paddle
move_right, move_left = False, False
# Movimiento de la pelota
speed_x, speed_y = 3, 3


class GameSprite():
    def __init__(self, sprite_image, x_pos, y_pos, sprite_width, sprite_height):
        self.width = sprite_width
        self.height = sprite_height
        self.image = pygame.transform.scale(pygame.image.load(sprite_image), (self.width, self.height))
        self.rect = pygame.Rect(x_pos, y_pos, sprite_width, sprite_height)
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Metodo que nos permite establecer colisiones entre objetos
    def collidepoint(self, x_pos, y_pos):
        return self.rect.collidepoint(x_pos, y_pos)
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# Main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Arkanoid')

# Creando instancias de objetos
ball = GameSprite('mario.png', 250, 10, 50, 50)
paddle = GameSprite('warp_pipe.png', 160, 450, 100, 50)

# Creacion de enemigos
enemy_x, enemy_y = 5, 5
count = 9
monsters = []

for i in range(3):
    y = (55 * i) + enemy_y
    x = (27.5 *i) + enemy_x

    for enemy in range(count):
        enemy = GameSprite('goomba.png', x, y, 50, 50)
        monsters.append(enemy)
        x += 55
    count -= 1
        
# Game Loop
clock = pygame.time.Clock()
running = True
finish = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Manejo de evento (presionar una tecla)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_a:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_a:
                move_left = False        
        
    
    # Establecer movimiento del paddle
    if move_right:
        paddle.rect.x += 3
    elif move_left:
        paddle.rect.x -= 3

    # Condicion de ejecucion:
    if not finish:
        # Incorporando elementos en pantalla
        screen.fill(BACKGROUND)
        for monster in monsters:
            monster.draw()
            
        ball.draw()
        paddle.draw()
        
        # Establecer movimiento de la pelota
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        # Colision de la pelota con los limites de la pantalla
        if ball.rect.y < 0:
            speed_y *= -1
            
        if ball.rect.x < 0 or ball.rect.x > 450:
            speed_x *= -1
        
        # Colision de la pelota con el paddle
        if ball.colliderect(paddle.rect):
            speed_y *= -1
            
    pygame.display.update()
    clock.tick(60)

pygame.quit()