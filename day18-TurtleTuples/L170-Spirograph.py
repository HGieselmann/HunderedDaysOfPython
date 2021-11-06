import random
import turtle
from turtle import Turtle
from turtle import Screen

def drawCircle(turtle, substeps, length, rotationStep):
    for i in range(substeps):
        turtle.forward(length)
        turtle.left(360 / substeps)
    turtle.left(rotationStep)


def randomColor():
    return random.randrange(50, 100)/100, random.randrange(50, 100)/100, random.randrange(50, 100)/100



timmy = Turtle()
timmy.pensize(2)
for i in range(36):
    timmy.color(randomColor())
    drawCircle(timmy, 30, 20, 360/36)


screen = Screen()
screen.exitonclick()


