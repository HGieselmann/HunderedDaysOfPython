import random
from turtle import Turtle
from turtle import Screen
import colorgram

STEPSIZE = 50

def createLineDots(turtle, stepsize):
    turtle.dot()
    for i in range(9):
        col = (random.choice(colors).rgb.r / 255, random.choice(colors).rgb.g / 255, random.choice(colors).rgb.b / 255)
        turtle.color(col)
        turtle.forward(stepsize)
        turtle.dot()


def switchLine(turtle, direction, stepsize):
    turtle.right(90 * direction)
    turtle.forward(stepsize)
    turtle.right(90 * direction)

colors = colorgram.extract('hirstColors.png', 10)

tim = Turtle()
tim.color((random.choice(colors).rgb.r / 255, random.choice(colors).rgb.g / 255, random.choice(colors).rgb.b / 255))
tim.pensize(10)
tim.penup()
tim.setpos(-250, 250)

for i in range(10):
    createLineDots(tim, STEPSIZE)
    if i % 2 == 0:
        switchLine(tim, 1, STEPSIZE)
    else:
        switchLine(tim, -1, STEPSIZE)

tim.hideturtle()

screen = Screen()
screen.exitonclick()

