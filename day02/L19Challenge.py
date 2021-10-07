userNumber = input("Enter a number between 10 and 99: ")
userNumberString = str(userNumber)
result = int(userNumberString[0]) + int(userNumberString[1])
print("The sum of both numbers is: " + str(result))