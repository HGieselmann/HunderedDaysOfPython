from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0,-320)
        self.setheading(90)
        self.color('green')
        self.speed(0)

    def move_forward(self):
        self.forward(10)

    def check_goal(self):
        if self.ycor() > 320:
            return True
