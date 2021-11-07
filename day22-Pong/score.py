from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorep1 = 0
        self.scorep2 = 0
        self.pu()
        self.color('white')
        self.hideturtle()
        self.goto(0, 200)

    def update_score(self):
        self.clear()
        self.write(f"Player 1: {self.scorep1}    Player 2: {self.scorep2}", font=('courier', 14, 'bold'), align='center')
