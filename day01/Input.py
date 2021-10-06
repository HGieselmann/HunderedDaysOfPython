# Greeting the user in one line.
print("Hello " + input("What is your name?\n"))

# Lesson 10 Challenge, count the length of a user name
print(len(input("What is your name again? I will print it's length: ")))

name = input("I forgot again. What was your name?")
print(f"Oh right... " + name + " it was!")
#print("The length of your name is " + (len(name)) + ". In case you did not know.")

#Lesson 12 Challenge: Switch values:
a = input("Value A: ")
b = input("Value B: ")
print("ValueA is: " + a)
print("ValueB is: " + b)

# switch
c = a
a = b
b = c
print("Value A is now: " + a)
print("Value B is now: " + b)