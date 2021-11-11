from turtle import Screen
from turtle import Turtle
import pandas as pd


screen = Screen()
image = ('blank_states_img.gif')
screen.addshape(image)
screen.title('U.S. States Game')
screen.setup(width=725, height=491)
turtle = Turtle(image)

naming_turtle = Turtle()
naming_turtle.penup()

state_data = pd.read_csv('50_states.csv')
game_running = True
while game_running:
    answer_state = screen.textinput("Guess the State", "What is another state name?").title()
    if state_data['state'].to_list().__contains__(answer_state):
        print("exists.")
        # Get row
        specific_state_data = state_data[state_data.state == answer_state]
        # Access data on row
        print(int(specific_state_data.x), int(specific_state_data.y))
        naming_turtle.goto(int(specific_state_data.x), int(specific_state_data.y))

        naming_turtle.dot()
    else:
        print("does not exist")
        game_running = False

screen.exitonclick()


