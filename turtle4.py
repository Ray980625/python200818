import turtle

turtle.shape('turtle')
turtle.penup()
sive = 20
for i in range(30):
    turtle.stamp()
    sive = sive + 3
    turtle.forward(sive)
    turtle.right(24)
turtle.done()