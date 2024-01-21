
from turtle import *

# 1.2 ⭐ Cuadrado y triangulo
pensize(2)
color("green")
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)


left(90)
color("yellow")
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
exitonclick()

# 2.4 Dibujando un Barco
def ship():
    color('light blue')
    pensize(5)
    forward(50)
    left(180-45)
    forward(70)
    left(180-45)
    forward(50)
    color('black')
    pensize(2)
    forward(30)
    right(90)
    forward(45)
    left(180-45)
    forward(50)
    left(45)
    forward(80)
    left(45)
    forward(50)
    left(180-45)
    forward(105)

#dibujar una onda, no cambiar
penup()
goto(-110,-25)
pendown()
color("blue")
pensize(2)
left(45)
speed(0)
i=0
while i<20:
    forward(10)
    right(90)
    forward(10)
    left(90)
    i=i+1
right(45)

#dibujar un barco
penup()
goto(0,50)
pendown()
ship()
exitonclick()

# 2.5 Tres Barcos:

def ship():
    color('light blue')
    pensize(5)
    forward(50)
    left(180-45)
    forward(70)
    left(180-45)
    forward(50)
    color('black')
    pensize(2)
    forward(30)
    right(90)
    forward(45)
    left(180-45)
    forward(50)
    left(45)
    forward(80)
    left(45)
    forward(50)
    left(180-45)
    forward(105)


penup()
goto(0,-30)
pendown()
ship()
penup()
goto(130,130)
pendown()
right(180)
ship()
penup()
goto(-130,130)
pendown()
right(180)
ship()
exitonclick()

# 2.1 ⭐  Multiples Circulos

pensize(2)
color("black")
begin_fill()
circle(60)
end_fill()
penup()


color("red")
goto(100,100)
pendown()
begin_fill()
circle(20)
end_fill()
penup()


color("green")
goto(-100,-100)
pendown()
begin_fill()
circle(30)
end_fill()
penup()


color("blue")
goto(-100,100)
pendown()
begin_fill()
circle(40)
end_fill()
penup()


color("yellow")
goto(100,-100)
pendown()
begin_fill()
circle(80)
end_fill()


exitonclick()

# 2.2 :star: Dibujando un abanico:

def dibujar_cuadrado(angulo):
    color('pink')
    pensize(2)
    left(angulo)
    for i in range(4):
        forward(100)
        left(90)

for i in range(5):
    dibujar_cuadrado(15)

exitonclick()