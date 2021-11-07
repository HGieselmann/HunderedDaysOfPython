import time
from turtle import Turtle, Screen, forward
from Snake import Snake


snake = Snake(20)
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The ultimate Snake Game")
screen.listen()
screen.onkey(snake.go_north, 'w')
screen.onkey(snake.go_east, 'd')
screen.onkey(snake.go_south, 's')
screen.onkey(snake.go_west, 'a')

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()


screen.exitonclick()
