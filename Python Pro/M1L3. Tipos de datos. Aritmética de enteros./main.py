number1 = '5.78'
number2 = 6
text = "Hola #"

anwswer = (int(float(number1))//number2)+15
number3 = text+str(anwswer)
print(type(number3))

# = = = = = = = = = = = = = #

num1 = '7'
num2 = 3.4
num3 = num1
text = num2
op1 = num2 * int(text) + float(num1)
op2 = str(int(op1)) + num1 * int(num3)
op3 = text + num3
op4 = op1 * int(op2)//op3
print(op4)
