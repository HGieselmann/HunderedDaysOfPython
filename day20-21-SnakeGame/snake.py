from turtle import Turtle

# Doing constants, as Angela did...
NORTH = 90
EAST = 0
SOUTH = 270
WEST = 180


class Snake:
    def __init__(self, stepsize):
        self.stepsize = stepsize
        self.length = 3
        self.body = []
        self.create_body()
        self.positions = []

    def create_body(self):
        for i in range(3):
            self.body.append(Turtle())
            self.body[i].color("white")
            self.body[i].shape("turtle")
            self.body[i].turtlesize(self.stepsize / 25)
            self.body[i].pu()
            self.body[i].backward(i * self.stepsize)

    def go_north(self):
        if not self.body[0].heading() == SOUTH:
            self.body[0].setheading(NORTH)

    def go_east(self):
        if not self.body[0].heading() == WEST:
            self.body[0].setheading(EAST)

    def go_south(self):
        if not self.body[0].heading() == NORTH:
            self.body[0].setheading(SOUTH)

    def go_west(self):
        if not self.body[0].heading() == EAST:
            self.body[0].setheading(WEST)

    def move_snake(self):
        self.update_positions()
        self.move_head()
        self.move_snake_body()

    def update_positions(self):
        self.positions = []
        for segment in self.body:
            self.positions.append(segment.pos())

    def move_head(self):
        self.body[0].forward(20)

    def move_snake_body(self):
        for i in range(1, len(self.body)):
            self.body[i].setpos(self.positions[i - 1])

    def add_segment(self):
        new_segment = Turtle('turtle')
        new_segment.color("white")
        new_segment.shape("turtle")
        new_segment.turtlesize(self.stepsize / 25)
        new_segment.pu()
        self.body.append(new_segment)

    def hit_walls(self):
        head_position = self.body[0].position()
        if head_position[0] > 300 or head_position[0] < -300 or head_position[1] > 300 or head_position[1] < -300:
            return True

    def hit_self(self):
        head_position = self.body[0].position()
        for i in range(1, len(self.body)):
            if self.body[i].distance(head_position) < 1:
                return True


