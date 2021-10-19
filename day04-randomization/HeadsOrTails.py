import random
running = True

while(running):
    userInput = input("You want me to toss a coin? y,n ")
    if userInput.lower() ==  "y":
        coin_toss = random.random()
        if coin_toss < 0.5:
            print("Heads!")
        else:
            print("Tails!")
    elif userInput.lower() == "n":
        running = False
        print("Ohh... okay... \nThanks for playing!")
    else:
        print("I did not understand. Enter 'n' or 'y'. ")
