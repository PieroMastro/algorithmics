from turtle import *

# Ciclos en Turtle:

def draw_star():
    begin_fill()
    for i in range(5):
        forward(150)
        left(144)
    end_fill()

def draw_circles():
    size = 10
    for i in range(7):
        circle(size)
        size += 10

def draw_triangle():
    color('blue')
    for i in range(3):
        forward(100)
        left(120)

def sun():
    begin_fill()
    for i in range(18):
        forward(150)
        left(100)
    end_fill()

color('yellow')
speed(10)
sun()

hideturtle()
exitonclick()