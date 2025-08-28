def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

print("Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Operation: ")

if op == "+":
    print("Addition: ", add(a, b))
elif op == "-":
    print("Subtraction: ", subtract(a, b))
elif op == "*":
    print("Multiplication: ", multiply(a, b))
elif op == "/":
    print("Division: ", divide(a, b))
else:
    print("Invalid Operation")

    



    


