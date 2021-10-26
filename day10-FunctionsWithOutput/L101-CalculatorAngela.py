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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
for symbol in operations:
    print (symbol)
operation_symbol = input("Pick an operation form the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")