# The most important Datatypes in python are:
# String, Int, Float and boolean
# if we write long integers we can split these using underscore:
myInt = 123_456_789
myFloat = 1.234
myString = "123"
byBoolean = True

# Functions expect a certain type specifically. If this does not match, it will error out
# because we can concatenate strings with string and not with intgers.
# In these cases we need to convert between types, by using the type as a function
num_char = len(input("What is your name?"))
print("Length of your name: " + str(num_char))

#We can check the type using type()
print(type(num_char))