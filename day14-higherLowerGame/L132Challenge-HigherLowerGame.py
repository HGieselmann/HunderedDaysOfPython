# My implementation of the higher lower game

import random
import provided_game_data

def find_random_entry(other_number):
    if other_number == 0:
        return random.randint(1, len(provided_game_data.data) - 1)
    else:
        numbers_equal = True
        while numbers_equal:
            b_number = random.randint(1, len(provided_game_data.data) - 1)
            if other_number != b_number:
                numbers_equal = False
            return b_number


def print_entry(entry_number, string):
    print(f"{string}: {provided_game_data.data[entry_number]['name']}, a {provided_game_data.data[entry_number]['description']} from {provided_game_data.data[entry_number]['country']}")


def test_result(user_choice):
    if user_choice == "a":
        return provided_game_data.data[a_number]['follower_count'] > provided_game_data.data[b_number]['follower_count']
    else:
        return provided_game_data.data[a_number]['follower_count'] < provided_game_data.data[b_number]['follower_count']


score = 0
print("Welcome to the higher/lower game!")
print("You have to guess which superstar has more followers!")
a_number = find_random_entry(0)

game_running = True
while game_running:
    b_number = find_random_entry(a_number)
    print_entry(a_number, "A")
    print_entry(b_number, "B")


    choice = input("Who do you think has more followers? (A,B) ").lower()
    result = test_result(choice)
    if result:
        a_number = b_number
        print("Correct!")
        score +=1
        print(f"Your score is {score}")
    else:
        print("You lose!")
        game_running = False





