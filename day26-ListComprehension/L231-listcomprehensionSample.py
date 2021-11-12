# basic structure
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers) # returns [2, 3, 4]

name = "Angela"
new_name = [letter for letter in name]
print(name)

doubled_numbers = [n * 2 for n in range(1, 6)]
print(doubled_numbers)


# Conditional List Comprehensions
# new_list = [item for item in list if test]

names = ['Alex', 'Beth', 'Frank', 'Paul', 'Maximilian']
short_names = [name for name in names if len(name) < 5]
print(short_names)

number_set = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n * n for n in number_set]
print(squared_numbers)

even_numbers = [n for n in number_set if n%2 == 0]
print(even_numbers)

with open('file1.txt') as file:
    number_set_one = file.readlines()
with open('file2.txt') as file2:
    number_set_two = file2.readlines()

filtered_numbers = [int(number) for number in number_set_one if number in number_set_two]
print(filtered_numbers)