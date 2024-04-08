from turtle import *

# 2/2
x_position = 200
y_position = 200
score = 0

#1/2
class Sprite(Turtle):
    def __init__(self, x, y, color='black', shape= 'circle', step= 10):
        super().__init__()
        self.penup()
        self.speed(0) # se implementa para que el jugador aparezca en el punto
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step
    # 1/2
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    # 2/2
    def detect_colission(self, sprite):
        distance = self.distance(sprite.xcor(), sprite.ycor())

        if distance < 30:
            return True
        else:
            return False

    # 2/2
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start       
        self.x_end = x_end
        self.y_end = y_end
        
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    # 2/2
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

    
# 1/2
player = Sprite(0, 0, 'green')
leo = Sprite(-x_position, y_position, 'blue','square', 20)
rafa = Sprite(x_position, -y_position, 'red', 'square', 20)
goal = Sprite(200, 200, 'grey', 'triangle')

# 2/2
leo.set_move(-200, 0, 200, 0)
rafa.set_move(200, 70, -200, 70)

# 1/2
screen = player.getscreen()
screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_down, 's')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')

# cont. 2/2
while score < 3:
    rafa.make_step()
    leo.make_step()

    if player.detect_colission(goal):
        score += 1
        player.goto(0, -100)
    elif player.detect_colission(rafa) or player.detect_colission(leo):
        goal.hideturtle()
        break
# 2/2
if score == 3:
    rafa.hideturtle()
    leo.hideturtle()
    player.hideturtle()
    goal.goto(0,0)
    goal.hideturtle()
    goal.write("GANASTE!", font=("Verdana", 20, "bold"), align='center')
