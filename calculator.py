def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
num1 = 5
operator = *
num2 =4
if operator == "+":
    print("Result:", add(num1, num2))
elif operator == "-":
    print("Result:", subtract(num1, num2))
elif operator == "*":
    print("Result:", multiply(num1, num2))
elif operator == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operator")
