# 1 can cover 5sqm of wall
import math


def greet():
    print("Welcome to the can amount calculator!")


def calculate_area():
    height = float(input("Please enter the wall height: "))
    width = float(input("Please enter the wall width: "))
    area = height * width
    return area


def calculate_cans(area):
    cans = area / 5
    return math.ceil(cans)


def print_result(cans):
    print(f"You will need {cans} cans to cover your wall!")


area = calculate_area()
cans = calculate_cans(area)
print_result(cans)
