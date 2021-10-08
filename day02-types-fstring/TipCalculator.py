print("Welcome to the quick tip calculator!")
bill = input("What was the total bill? ")
people = input("How many people to split the bill? ")
percentage = input("What percentage would you like to give? 10, 12 or 15 ")
result = (float(bill) / float(people) * (float(percentage)/100))

print("Each person should pay " + str(result) + ".")