from turtle import *
from random import randint
from time import sleep

def move(x, y):
    penup()
    goto(x, y)
    pendown()

def set_turtle(color, name, x, y):
    # Create a new turtle with the given color, name, and position
    turtle = Turtle()
    turtle.name = name
    turtle.color(color)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    return turtle

def start_race(turtle):
    # Move the turtle forward by a random distance
    turtle.forward(randint(1, 5))

def finish_race(turtle_1, turtle_2, finish):
    # Check if either turtle has crossed the finish line
    return turtle_1.xcor() >= finish or turtle_2.xcor() >= finish

def get_winner(turtle_1, turtle_2):
    # Return the turtle that has crossed the finish line first
    if turtle_1.xcor() >= turtle_2.xcor():
        return turtle_1
    else:
        return turtle_2

def start_message():
    # Display bet announce
    move(0, 50)
    write(f"HAGAN SUS APUESTAS!", align="center", font=("Arial", 24, "bold"))
    hideturtle()
    sleep(1.5)
    clear()


def show_winner(winner):
    # Display the winner's name
    move(0, 50)
    write(f"Ganador: {winner.name}!", align="center", font=("Arial", 24, "bold"))
    hideturtle()

finish = 200
mike = set_turtle('orange', 'Mike', -200, 0)
rafa = set_turtle('red', 'Rafa', -200, -50)
bet = start_message()

while True:
    start_race(rafa)
    start_race(mike)
        
    if finish_race(rafa, mike, finish):
        winner = get_winner(rafa, mike)
        show_winner(winner)
        break

sleep(0.1)

exitonclick()

