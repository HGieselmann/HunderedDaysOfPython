import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '_']

password_string = ""
pass_length = int(input("How long should the password be? "))
number_count = int(input("How many numbers do you want? "))
symbol_count = int(input("How many symbols do you want? "))
letter_count = (pass_length - number_count) - symbol_count

for n in range(0, pass_length):
    if n < number_count:
        password_string += (numbers[random.randint(0, len(numbers) - 1)])
    elif n < number_count + symbol_count:
        password_string += (symbols[random.randint(0, len(symbols) - 1)])
    else:
        password_string += (letters[random.randint(0, len(letters) - 1)])

password_list = list(password_string)
random.shuffle(password_list)
password_string = "".join(password_list)

print("Your password is: ")
print(password_string)