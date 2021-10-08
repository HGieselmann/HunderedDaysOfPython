## Added elif forom lessen 29
print("Wecome to the roller coaster!")
height = int(input("What is your height in cm?"))
age = int(input("How old are you?"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("Please pay 4$.")
    elif age <= 18:
        print("The fee is 5$")
    else:
        print("The fee is 7.50$ for adults.")
else:
    print("Sorry, you have to grow taller before you can ride.")