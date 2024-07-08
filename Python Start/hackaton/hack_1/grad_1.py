# Soluciones a las tareas de la primera ronda

# 3. ========================================
yes = "¡Correcto! ¡Únete a nuestra fiesta!"
no = "¡No conoces la contraseña! ¡Guardias!"
answer = input("¡Detente! ¡Dime la contraseña!")
if answer == "amigo":
    print(yes)
else:
    print(no)

# 4. ========================================
number = int(input("Ingresa un número"))
if number > 0:
    print("Número",number,"positivo.")
else:
    if number < 0:
        print("Número",number,"negativo.") 
    else:
        print("¡Es cero!")
        
        
# 5. ========================================
number1 = int(input("Ingresa el primer número"))
number2 = int(input("Ingresa el segundo número"))
while number2 >= number1:
    print(number1)
    number1 = number1 + 1


# 9. ========================================
def more(a, b):
    if a > b:
        print("a es mayor que b")
    if a < b:
        print("a es menor que b")
    if a == b:
        print("a es igual que b")    

a = int(input("Ingresar número a:"))
b = int(input("Ingresar número b:"))
more(a, b)


# 10. ========================================
def maximum(name1, height1, name2, height2):
    if height1 > height2:
        print(name1 + " es más alto que " + name2 + " por " + str((height1 - height2)) + " cm")
    else:
        if height2 >height1:
            print(name2 + " es más alto que " + name1 + " por " + str((height2 - height1)) + " cm")
        else:
            print(name1 + " y " + name2 + " son de la misma altura.")

name1 = input("Nombre de primera persona")
height1 = int(input("Altura de primera persona"))
name2 = input("Nombre de segunda persona")
height2 = int(input("Altura de segunda persona"))
maximum(name1, height1, name2, height2)


# 12. ========================================
from turtle import*

t = Turtle()
t.penup()
t.goto(-100,0)
t.pendown()
t.pensize(2)
t.color("yellow")
i=0
t.begin_fill()

while i<5:
    t.forward(200)
    t.left(144)
    i=i+1
t.end_fill()

t.hideturtle()  
exitonclick()


# 15. ========================================
class Animal():
    def __init__(self, species, voice, size):
        self.species = species
        self.voice = voice
        self.size = size
        
    def make_voice(self):
        print(self.voice)

cat = Animal('gato','miau', 'medio')    
cow = Animal('vaca', 'moo', 'grande')  

cow.make_voice()
cat.make_voice()


# 17. ========================================
from turtle import *

pensize(5)
color('gray')

forward(30)
left(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)

hideturtle()
exitonclick()


# 19. ========================================
from turtle import *

def square():
    color("steelblue")
    pensize(3) 
    i = 0
    while i < 4:
        forward(50)
        left(90)
        i = i + 1
n = 0

while n < 8:
    square() 
    left(45)       
    n = n + 1

hideturtle()
exitonclick()


# 20. ========================================
from turtle import *

def square(col):
    color(col)
    i = 0
    while i < 4:
        forward(100)
        left(90)
        i = i + 1

def star(col):
    color(col)
    for i in range(5):
        forward(100)
        left(145)

answer = int(input("¿Qué quieres dibujar? Escribe un número en la respuesta. 1 - cuadrado, 2 - estrella"))
col = input("Ingresa el color")

if answer == 1:
    square(col)
else:
    if answer == 2:
        star(col)
    else:
        print("¡Un número incorrecto ha sido ingresado!")

exitonclick()
