from turtle import Turtle
from turtle import Screen

timmy = Turtle()

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()

