import time
from turtle import Screen
from score import Score
from centerline import Centerline

from ball import Ball
from paddle import Paddle

player_1 = Paddle(1)
player_2 = Paddle(-1)
paddles = [player_1, player_2]
ball = Ball()
scoreboard = Score()
centerline = Centerline()

screen = Screen()
screen.setup(width=640, height=480)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
screen.onkey(fun=player_1.set_north, key='w')
screen.onkey(fun=player_1.set_south, key='s')
screen.onkey(fun=player_2.set_north, key='i')
screen.onkey(fun=player_2.set_south, key='k')
screen.onkey(fun=screen.bye, key='y')


game_running = True
while game_running:
    time.sleep(0.05)
    screen.update()
    player_1.move()
    player_2.move()
    ball.bounce_paddles(paddles)
    ball.move()

    bounds = ball.check_horizontal_bounds()
    if bounds == 1:
        scoreboard.scorep1 += 1
    elif bounds == 2:
        scoreboard.scorep2 += 1

    scoreboard.update_score()



screen.exitonclick()