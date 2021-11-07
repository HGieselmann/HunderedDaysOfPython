import time
from turtle import Turtle, Screen, forward
from snake import Snake
from food import Food
from scoreboard import Scoreboard


snake = Snake(20)
food = Food()
scoreboard = Scoreboard()


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
    if snake.hit_walls() or snake.hit_self():
        print("You died")
        scoreboard.game_over()
        game_running = False
        break

    if food.distance(snake.body[0].position()) < 15:
        food.goto_random_position()
        snake.add_segment()
        scoreboard.add_score()


screen.exitonclick()
