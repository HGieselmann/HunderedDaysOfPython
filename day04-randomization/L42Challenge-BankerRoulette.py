import random

bankers = []

user_input = input("Enter the names of the participants divided by ',': ")

names = user_input.split(',')
paying_participant = names[random.randint(0, len(names)-1)]

print(f"{paying_participant.strip()} has to pay the bill.")