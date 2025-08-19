#Simple Calculator

print("Welcome to Calculator!")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Choose Operation: +, -, *, /")
op = input("Enter Operation: ")

if op == "+":
    print("Addition = ", num1+num2)
elif op == "-":
    print("Subtraction = ", num1-num2)
elif op == "*":
    print("Multiplication = ", num1*num2)
elif op == "/":
    if num2 != 0:
        print("Division = ", num1/num2)
    else:
        print("Error: Division by Zero!")
else:
    print("Invalid Operation!")

        
    
