from turtle import Turtle
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.write('Score: ' + str(self.score), align='center', font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write('Score: ' + str(self.score), align='center')

    def game_over(self):
        self.goto(0,0)
        self.write('You died', align='center', font=('Courier', 24, 'bold'))
