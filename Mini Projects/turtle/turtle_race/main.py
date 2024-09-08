from turtle import *
from random import randint
from time import sleep


def get_turtle(color, x, y):
    turtle = Turtle()
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    return turtle

leo = get_turtle('blue', -200, 0)
rafa = get_turtle('red', -200, 50)
mike = get_turtle('orange', -200, -50)
pencil = get_turtle('grey', -150, 100)

def start_message():
    pencil.write('HAGAN SUS APUESTAS!', font = ('Arial', 20, 'normal'))
    pencil.hideturtle()
    sleep(1.5)
    pencil.clear()

    bet = input('Ingrese el nombre de la tortuga ganadora:').lower()

    return bet

bet = start_message()

print(bet)
