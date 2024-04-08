from turtle import *

x_position = 200
y_position = 200


class Sprite(Turtle):
    def __init__(self, x, y, color='black', shape= 'circle', step= 10):
        super().__init__()
        self.penup()
        self.speed(0) # se implementa para que el jugador aparezca en el punto
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())


player = Sprite(0, 0, 'green')
leo = Sprite(-x_position, y_position, 'blue','square', 20)
rafa = Sprite(x_position, -y_position, 'red', 'square', 20)
goal = Sprite(200, 200, 'grey', 'triangle')


screen = player.getscreen()
screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_down, 's')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')

