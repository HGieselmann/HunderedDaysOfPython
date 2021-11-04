import random
from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.pu()
timmy.backward(40)
timmy.left(90)
timmy.forward(250)
timmy.right(90)
timmy.pd()

for i in range(4,101):
    timmy.color(random.random(), random.random(), random.random())
    for j in range(0, i):
        timmy.forward(80)
        timmy.right(360/i)

screen = Screen()
screen.exitonclick()