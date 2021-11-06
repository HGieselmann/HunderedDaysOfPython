import random
from turtle import Turtle
from turtle import Screen

colors = ['red', 'green', 'blue']

def createTurtle():
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.pu()
    return turtle

def moveRandomly(turtle):
    turtle.forward(random.randint(0, 10))


def checkWinCondition(turtle):
    if turtle.xcor() > 200:
        return turtle.color()
    else:
        return False


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Bet", "Which turtle will win? (red, green, blue)").lower()


turtles = []
for i in range(3):
    turtles.append(createTurtle())
    turtles[i].color(colors[i])
    print("bam")

for i in range(len(turtles)):
    turtles[i].goto(-240, i * 20)

winner = False
while not winner:
    for turtle in turtles:
        moveRandomly(turtle)
        winner = checkWinCondition(turtle)
        if winner:
            break

if winner[0] == bet:
    print("You gessed correctly.")
else:
    print(f"You guessed false! The winner was: {winner[0]}")

screen.exitonclick()
