from turtle import Turtle
from turtle import Screen

tim = Turtle()

def moveForward():
    tim.forward(10)


def moveBackward():
    tim.backward(10)


def turnLeft():
    tim.left(5)


def turnRight():
    tim.right(5)


screen = Screen()
screen.listen()
screen.onkey(fun=moveBackward, key="s")
screen.onkey(fun=moveForward, key="w")
screen.onkey(fun=turnLeft, key="a")
screen.onkey(fun=turnRight, key="d")

screen.exitonclick()
