print("Welcome to Pizza Deliveries. Your best pizza around!")
size = input("What kind of pizza do you want? S, M, L ")
add_pepperoni = input("Do you want extrea pepperoni? yes no ")
extra_cheese = input("Do you want extra cheese? yes, no ")

price = 0

if size.lower() == "s":
    price = 15
elif size.lower() == "m":
    price = 20
else:
    price = 25

if add_pepperoni.lower() == "yes":
    if size.lower() == "s":
        price += 2
    else:
        price += 3

if extra_cheese.lower() == "yes":
    price += 1

print(f"Your pizza costs: {price}")