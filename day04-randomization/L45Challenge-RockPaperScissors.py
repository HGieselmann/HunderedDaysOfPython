import random

items = ["Rock", "Paper", "Scissors"]

row1 = ['Draw', 'Lose', 'Win']
row2 = ['Lose', 'Draw', 'Win']
row3 = ['Win', 'Draw', 'Lose']
matrix = [row1, row2, row3]

user_input = int(input("Choose your sign: 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_selection = random.randint(0,2)

print(f"You chose: {items[user_input]}. ")
print(f"The computer chose: {items[computer_selection]}. ")
result = matrix[user_input][computer_selection]