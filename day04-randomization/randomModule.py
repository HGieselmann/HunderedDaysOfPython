import random

#randint is inclusive
random_integer = random.randint(1, 10)
print(random_integer)

# this is not inclusive
random_float = random.random()
print(random_float)

random_float_large_range = random.random() * 10
print(random_float_large_range)