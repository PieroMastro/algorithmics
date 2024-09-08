from turtle import *

t = Turtle()
t.color('red')
t.speed(5)
t.width(5)
t.shape('circle')
t.pendown()

def drag(x, y):
    t.goto(x, y)
    
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def set_instructions():
    color('grey')
    penup()
    goto(0, 200)
    pendown()
    write('Simple Paint', align="center", font=("Arial", 20, "bold"))
    hideturtle()
    exitonclick()

set_instructions()    

scr = t.getscreen()
scr.onscreenclick(move)

t.ondrag(drag)

