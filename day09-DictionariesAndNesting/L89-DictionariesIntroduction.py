programming_dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code you can easily call over and over again",
    "Loop": "The action of doing things over and over again."
    }

# print an item inside a dictionary
print(programming_dict["Bug"])

# Add an item to an dictionary
programming_dict["Variable"] = "A way to store data inside your program"

# Edit an entry
programming_dict["Variable"] = "Store data inside your program"

# Wiping a dictionary
programming_dict = {}

# Looping through a dictionary - will give you the keys - tab into the dict to get Values
for thing in programming_dict:
    print(thing)
    print(programming_dict[thing])
