def add(a, b):
    """Add to values and return the result."""
    return a + b

def subtract(a, b):
    """Subtract two values and return the result."""
    return  a-b

def multiply(a, b):
    """Multiply two values and return the result."""
    return a * b

def divide(a, b):
    """Divide two values and return the result."""
    return a / b

continue_calculating = True


print("Welcome to the calculator program! ")
use_intermediate_result = False
while continue_calculating:
    operation = input("Please enter a an operand to select the operation you want to do: (+,-,*,/)")
    if use_intermediate_result:
        input_a = intermediate_result
    else:
        input_a = float(input("Please enter the first value: "))
    use_intermediate_result = False
    input_b = float(input("Please enter the second value: "))

    if operation == "+":
        intermediate_result = add(input_a, input_b)
    elif operation == "-":
        intermediate_result = subtract(input_a, input_b)
    elif operation == "*":
        intermediate_result = multiply(input_a, input_b)
    elif operation == "/":
        intermediate_result = divide(input_a, input_b)
    else:
        print("Operation input invalid.")

    print(f"Your result is {intermediate_result}.")
    user_input = input("Enter 'c' to continue with this result, 'n' to begin a new calculation, 'exit' to end.")
    if user_input == 'c':
        use_intermediate_result = True
    elif user_input == 'exit':
        continue_calculating = False


print("Thanks for using the simple python calculator.")



