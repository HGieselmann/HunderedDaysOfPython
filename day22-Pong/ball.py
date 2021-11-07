import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.direction = [10, 10]

    def move(self):
        self.check_vertical_bounds()
        self.goto(self.xcor() + self.direction[0], self.ycor() + self.direction[1])

    def check_vertical_bounds(self):
        if self.ycor() > 230 or self.ycor() < -230:
            self.direction[1] *= -1

    def check_horizontal_bounds(self):
        if self.xcor() > 320:
            time.sleep(3)
            self.goto(0,0)
            return 1
        elif self.xcor() < -320:
            time.sleep(3)
            self.goto(0, 0)
            return 2
        else:
            return 0

    def bounce_paddles(self, paddles):
        for paddle in paddles:
            for segment in paddle.segments:
                if segment.distance(self.position()) < 20:
                    if self.xcor() > 0:
                        self.direction[0] = -10
                    else:
                        self.direction[0] = 10
