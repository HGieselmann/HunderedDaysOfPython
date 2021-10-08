print("Welcome to treasure Island.")
print("Can you find the treasure?")
answer = input("You find yourself at a crossroad. Where do you want to go? 'Left' or 'right'?").lower()
if(answer == "left"):
    print("You end up at a huge lake which, you can barely see the other side. What do you do?")
    answer2 = input("Do you attempt to 'swim' or 'wait'?").lower()
    if (answer2 == "wait"):
        print("A tiny boat arrives and takes you directly to the treasure. You win.")
    else:
        print("You die.")
else:
    print("You die.")
