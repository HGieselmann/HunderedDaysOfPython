import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100!")
    computer_number = random.randint(1, 101)
    print(computer_number)


    print("Can you guess which?")
    difficulty = input("Choose your difficulty! (hard, easy): ").lower()
    if difficulty == "hard":
        guesses_left = 5
    else:
        guesses_left = 10

    guess_correct = False
    while not guess_correct and guesses_left > 0:
        user_guess = int(input("Enter your guess: "))
        if user_guess == computer_number:
            guess_correct = True
        elif user_guess < computer_number:
            print("Too low!")
            guesses_left -= 1
            print(f"You have {guesses_left} left.")
        else:
            print("Too high!")
            guesses_left -= 1
            print(f"You have {guesses_left} left.")

    if guess_correct:
        print("Congratulations!")
    else:
        print("Too bad. You loose!")

    if input("Do you want to play again? (yes/no) ") == "yes":
        play_game()

play_game()