def default_arguments(a=1, b="name"):
    print(f"{a} and {b}")


# We can pass arguments or leave them blank
default_arguments(2, "Frank")
default_arguments()


# unlimited positional arguments
def sum_unlimited_arguments(*args):
    sum = 0
    for n in args: # args is a tuple
        sum += n
    return sum


print(sum_unlimited_arguments(1, 2, 3))
print(sum_unlimited_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9))


# unlimited keyword arguments
def calculate(n, **kwargs):
    # kwargs is a dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)
    #get will return `none` if no value is supplied
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    return n





print(calculate(2, add=3, multiply=5))

