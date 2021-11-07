import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

player_1 = Paddle(1)
player_2 = Paddle(-1)
ball = Ball()

screen = Screen()
screen.setup(width=640, height=480)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
screen.onkey(fun=player_1.set_north, key='w')
screen.onkey(fun=player_1.set_south, key='s')
screen.onkey(fun=player_2.set_north, key='i')
screen.onkey(fun=player_2.set_south, key='k')


game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()
    player_1.move()
    player_2.move()
    ball.move()
    bounds = ball.check_horizontal_bounds()
    if bounds == 1:
        print("score player 1")
    elif bounds == 2:
        print("score player 2")



screen.exitonclick()