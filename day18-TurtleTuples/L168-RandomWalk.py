import random
from turtle import Turtle
from turtle import Screen

def rotateRandomly():
    randomValue = random.randint(0,4)
    if randomValue == 0:
        return 0
    if randomValue == 1:
        return 90
    if randomValue == 2:
        return 180
    else: return 270


# Angelas Random direction method
directions = [0, 90, 180, 270]
randomdirection = random.choice()


timmy = Turtle()
timmy.pensize(5)
timmy.speed(0)
while True:
    timmy.color(random.random(), random.random(), random.random())
    timmy.forward(10)
    #timmy.left(rotateRandomly())
    timmy.setheading(randomdirection)

screen = Screen()

