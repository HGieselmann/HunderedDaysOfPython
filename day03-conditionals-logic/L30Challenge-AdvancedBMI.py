print("Welcome to the advanced BMI Calculator.")
height = float(input("Please enter your height in m: "))
weight = float(input("Please enter your weight in kilos: "))
bmi = weight / (height * height)
bmi = round(bmi, 1)
print(f"Your BMI is : {bmi}.")

classification = ""
if bmi < 18.5:
    classification = "underweight"
elif bmi < 25:
    classification = "normal weight"
elif bmi < 30:
    classification = "overweight"
elif bmi < 35:
    classification = "obese"
else:
    classification = "clinically obese"

print(f"This means you are {classification}")