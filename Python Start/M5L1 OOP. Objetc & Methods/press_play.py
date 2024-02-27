from turtle import *


t1 = Turtle()
t1.color('red')


t2 = Turtle()
t2.color('green')
t2.left(120)


t3 = Turtle()
t3.color('blue')
t3.left(240)


t1.begin_fill()
t2.begin_fill()
t3.begin_fill()



for i in range(60):
    t1.forward(5)
    t1.left(5)
    t2.forward(5)
    t2.left(5)
    t3.forward(5)
    t3.left(5)


t1.end_fill()
t2.end_fill()
t3.end_fill()
