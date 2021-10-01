import turtle
import random

numb = random.randint(1, 100)
spin = random.randint(10, 90)
width1 = 10

script = True
while script:
    turtle.speed(2000)
    turtle.bgcolor("black")


    turtle.color("red")
    turtle.forward(numb)
    turtle.right(spin)
    turtle.circle(spin)
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)
        
    turtle.pencolor("red")
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)

    turtle.color("yellow")
    turtle.forward(numb)
    turtle.right(spin)
    turtle.circle(spin)
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)
        
    turtle.pencolor("red")
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)


    turtle.color("green")
    turtle.forward(numb)
    turtle.right(spin)
    turtle.circle(spin)
    for i in range(50):
        turtle.forward(numb)
        turtle.left(spin)
        
    turtle.pencolor("red")
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)

    turtle.color("blue")
    turtle.forward(numb)
    turtle.right(spin)
    turtle.circle(spin)
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)
        
    turtle.pencolor("red")
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)

    turtle.color("purple")
    turtle.forward(numb)
    turtle.right(spin)
    turtle.circle(spin)
    turtle.width(width1 + 1)
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)
        
    turtle.pencolor("red")
    for i in range(10):
        turtle.forward(numb)
        turtle.left(spin)