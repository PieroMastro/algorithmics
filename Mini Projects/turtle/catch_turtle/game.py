from turtle import *
from random import randint
from time import sleep

# Crear una instancia de la clase Turtle()
def make_turtle(color, shape):
    turtle = Turtle()
    turtle.color(color)
    turtle.shape(shape)
    turtle.pensize(4)
    turtle.speed(randint(1, 5))
    turtle.left(randint(0, 180))

    return turtle

# Logica de movimiento
def move_randomly(turtle):
    turtle.goto(randint(-x, x), randint(-y, y))
    turtle.left(randint(0, 180))

def catch_turtle(x, y, turtle):
    move_randomly(turtle)

# Ciclo de ejecucion
def game_loop(turtles, stop):
    while True:
        for turtle in turtles:
            turtle.forward(randint(1, 5))
            if abs(turtle.xcor()) > x or abs(turtle.ycor()) > y:
                turtle.write('Lo siento perdiste', align='center', font=('Arial', 16, 'bold'))
                return

# Creacion de objetos:
leo = make_turtle('blue', 'turtle')
rafa = make_turtle('red', 'turtle')
mike = make_turtle('orange', 'turtle')

# lista de tortugas:
turtles = [leo, rafa, mike]

x, y = 250, 250
stop = 250


leo.onclick(lambda x, y: catch_turtle(x, y, leo))
rafa.onclick(lambda x, y: catch_turtle(x, y, rafa))
mike.onclick(lambda x, y: catch_turtle(x, y, mike))

game_loop(turtles, stop)
mainloop()