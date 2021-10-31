import CoffeeMachineResources as CMR

machine_running = True
while machine_running:
    user_money = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    # TODO Prompt User what he likes
    user_drink = input("What would you like to drink? (Espresso, Latte, Cappuccino) ").lower()
    if user_drink == "off":
        machine_running = False
        continue  # ends the while loop
    elif user_drink == "report":
        CMR.print_report()
        continue

    if CMR.check_resources(user_drink):
        print(f"Can do! Please provide {CMR.cost(user_drink)}$.")
        for key in user_money:
            user_money[key] = int(input(f"Enter {key}: "))
        user_money_sum = CMR.sum_money(user_money)
        print(f"You entered: {user_money_sum}.")
        if user_money_sum == CMR.MENU[user_drink]['cost']:
            CMR.make_drink(user_drink)
            CMR.profit += CMR.MENU[user_drink]['cost']
        elif user_money_sum >= CMR.MENU[user_drink]['cost']:
            CMR.make_drink(user_drink)
            CMR.profit += CMR.MENU[user_drink]['cost']
            print(f"Here is your change: {CMR.give_change(user_money_sum, user_drink)}.")
        else:
            print(f"Not enough money. Here is your money back. Returning: {user_money_sum}")
    else:
        print("Not enough resources...")
