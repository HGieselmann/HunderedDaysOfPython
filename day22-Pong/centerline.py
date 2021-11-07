from turtle import Turtle


class Centerline(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 240)
        self.color('white')
        self.setheading(270)
        self.speed('fastest')
        for _ in range(0, 48):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
