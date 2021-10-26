import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def does_the_user_want_to_play():
    user_wants_to_play = input("Do you want to play a round of back jack? (yes/no) ").lower()
    if user_wants_to_play == "yes":
        return True
    elif user_wants_to_play == "no":
        return False
    else:
        print("Invalid Input - assuming false.")


def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum


def ask_for_another_card():
    get_another_card = input("Do you want another card? (yes, no) ").lower()
    if get_another_card == "no":
        return False
    elif get_another_card == "yes":
        return True
    else:
        print("Invalid Input - assuming False.")
        return False


def print_current_score(cards):
    print(f"Your cards are: {cards}, current score: {sum_cards(cards)}")


def deal_new_card():
    return cards[random.randint(0, len(cards) - 1)]
