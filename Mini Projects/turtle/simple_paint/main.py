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


# Nuevas funciones:

def set_green():
    t.color('green')

def step_right():
    t.goto(t.xcor() + 5, t.ycor())

# Main 
set_instructions()    

display = t.getscreen()
display.onscreenclick(move)

t.ondrag(drag)

# Implementacion de nuevas mecanicas
display.listen()
display.onkey(step_right, "right")
display.onkey(set_green, "g")

display.mainloop()
