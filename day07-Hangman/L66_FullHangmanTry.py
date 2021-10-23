import random

game_running = True
player_won = False
lives = 5

easy_words = ["hello", "dance", "walk"]
medium_words = ["radiator", "kitchen", "bathroom"]
difficult_words = ["xenos", "excavator", "synchronisation"]

selected_word = ""
current_word = ""


def prepare_current_word():
    word = ""
    for n in range(0, len(selected_word)):
        word += "_"
    return word


def choose_difficulty():
    word_list = []
    user_input = input("Please enter your preferred difficulty: 1-3 ")
    if user_input == "1":
        word_list = easy_words
    elif user_input == "2":
        word_list = medium_words
    else:
        word_list = difficult_words
    selected_word = random.choice(word_list)
    # selected_word = word_list[random.randint(0, len(word_list) - 1)]

    return selected_word


def display_current_word():
    print(current_word)


def ask_for_character():
    got_valid_character = False
    while not got_valid_character:
        character = input("Please guess a character: ").lower()
        if len(character) > 1 or len(character) < 1:
            print("Please enter a valid character!")
        else:
            got_valid_character = True
    return character


def check_if_character_in_word():
    global character
    global current_word
    character_found = False
    for n in range(0, len(selected_word)):
        if selected_word[n] == character:
            character_found = True
    if character_found:
        print("That's correct!")
        current_word = update_word(current_word)
        return True
    else:
        return False


def update_word(current_word):
    current_word_list = list(current_word)
    for n in range(0, len(current_word_list)):
        if selected_word[n] == character:
            current_word_list[n] = character
    return "".join(current_word_list)


def loose_life():
    print("Sorry, this is not the case.")
    global lives
    lives = lives - 1
    if lives <= 0:
        global game_running
        game_running = False
    else:
        print(f"You have still {lives} lives left.")


def check_win_condition():
    global current_word
    if current_word.__contains__("_"):
        return False
    else:
        return True


selected_word = choose_difficulty()
current_word = prepare_current_word()
display_current_word()
while game_running:

    character = ask_for_character()
    character_in_word = False
    character_in_word = check_if_character_in_word()
    if character_in_word:
        player_won = check_win_condition()
        if player_won:
            print("Congratulations. You won!")
            game_running = False
        else:
            display_current_word()
    else:
        loose_life()

if not player_won:
    print("Sorry, you lost the game...")
