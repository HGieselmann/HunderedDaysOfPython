from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.length = 3
        self.segments = []
        self.create_segments()

        self.__SPEED = 15


    def create_segments(self):
        for i in range(0, self.length):
            segment = Turtle()
            segment.speed('fastest')
            segment.penup()
            segment.color('white')
            segment.shape('square')
            segment.setheading(90)
            segment.goto((-290 * self.side)-2, i * 20)
            self.segments.append(segment)

    def move(self):
        heading = self.segments[0].heading()
        if self.segments[2].ycor() > 230 and heading == 90:
            pass
        elif self.segments[0].ycor() < -230 and heading == 270:
            pass
        else:
            for seg in self.segments:
                seg.forward(self.__SPEED)

    def set_north(self):
        for seg in self.segments:
            seg.setheading(90)

    def set_south(self):
        for seg in self.segments:
            seg.setheading(270)

