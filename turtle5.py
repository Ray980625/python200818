import turtle
a = turtle.Turtle()
b = int(input('邊數:'))
for i in range(b):
    a.forward(100)
    a.left(360/b)