user_year = int(input("Enter a year to check if it is a leap year: "))
if(user_year % 4 == 0):
    if(user_year % 100 == 0):
        if user_year % 400 == 0:
            print("This is a leap year!")
        else:
            print(f"{user_year} is not a leap year...")
    else:
        print(f"{user_year} is not a leap year.")

else:
    print(f"{user_year} is not a leap year")