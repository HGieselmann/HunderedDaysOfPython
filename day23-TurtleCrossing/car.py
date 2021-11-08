from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(random.random(), random.random(), random.random())
        self.goto(random.randint(-640, 640), random.randint(-300, 300))
        self.setheading(180)
        self.speed(0)

    def move_forward(self):
        self.forward(5)
        if self.xcor() < -650:
            self.setposition(650, random.randint(-300, 300))

    def check_collision(self, turtle):
        if self.distance(turtle) < 22:
            return True
