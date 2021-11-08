import time
from turtle import Screen
from player import Player
from car import Car

def resetGame():
    global game_running
    game_running = True
    player = Player()
    return player


screen = Screen()
screen.setup(width=1280, height=720)
screen.tracer(0)

player = resetGame()

screen.listen()
screen.onkey(fun=player.move_forward, key='space')

cars = []
for i in range(50):
    cars.append(Car())

game_running = True
while game_running:
    for car in cars:
        car.move_forward()
        if car.check_collision(player):
            game_running = False

    screen.update()
    if player.check_goal():
        game_running = False
    time.sleep(0.05)

screen.exitonclick()
