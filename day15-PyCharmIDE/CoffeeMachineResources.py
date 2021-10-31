MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0
}


def print_report():
    for key in resources:
        print(f"{key.title()}: {resources[key]}")


def check_resources(key):
    enough_res = True
    if MENU[key]['ingredients']['water'] > resources['water']:
        enough_res = False
    if MENU[key]['ingredients']['coffee'] > resources['coffee']:
        enough_res = False
    if "milk" in MENU[key]['ingredients']:
        if MENU[key]['ingredients']['milk'] > resources['coffee']:
            enough_res = False
    return enough_res


def cost(drink):
    return MENU[drink]['cost']


def sum_money(money):
    sum = 0
    for key in money:
        if key == "quarters":
            sum += money[key] * 0.25
        elif key == "dimes":
            sum += money[key] * 0.1
        elif key == "nickles":
            sum += money[key] * 0.05
        else:
            sum += money[key] * 0.01

    return round(sum,2)


def make_drink(drink):
    print(f"Here is your drink: {drink}.")
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    if "milk" in MENU[drink]['ingredients']:
        resources['milk'] -= MENU[drink]['ingredients']['milk']


def give_change(money, drink):
    return round(money - MENU[drink]['cost'], 2)

