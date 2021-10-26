import blackJackHelpers
import random

# The challenge assumes an infinite deck, see here:
# https://replit.com/@appbrewery/blackjack-start


game_running = blackJackHelpers.does_the_user_want_to_play()
while game_running:
        player_cards = []
        dealer_cards = []

        for i in range(0,2):
            player_cards.append(blackJackHelpers.deal_new_card())
            dealer_cards.append(blackJackHelpers.deal_new_card())
        blackJackHelpers.print_current_score(player_cards)
        print(f"The dealers first card is {dealer_cards[0]}")

        get_another_card = True
        while get_another_card:
            get_another_card = blackJackHelpers.ask_for_another_card()
            if not get_another_card:
                continue
            else:
                player_cards.append(blackJackHelpers.deal_new_card())
                blackJackHelpers.print_current_score(player_cards)
                if blackJackHelpers.sum_cards(player_cards) > 21:
                    get_another_card = False
        while blackJackHelpers.sum_cards(dealer_cards) < 17:
            dealer_cards.append(blackJackHelpers.deal_new_card())

        player_score = blackJackHelpers.sum_cards(player_cards)
        dealer_score = blackJackHelpers.sum_cards(dealer_cards)

        print(f"Your final score is {player_score}")
        print(f"Dealers final score is {dealer_score}")
        if player_score > 21 >= dealer_score:
            print("You lose")
        elif player_score > 21 and dealer_score > 21:
            print("Draw!")
        elif player_score == dealer_score:
            print("Draw!")
        elif player_score < dealer_score < 22:
            print("You lose.")
        else:
            print("You win!")

        if input("Do you want to play another round? (yes/no) ").lower() == "no":
            game_running = False
