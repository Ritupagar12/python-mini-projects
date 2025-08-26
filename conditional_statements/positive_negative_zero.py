#Checks if a number is positive, negative or zero.
number = int(input("Enter a number: "))

if(number > 0):
    print(f"{number} is a Positive Number")
elif(number < 0):
    print(f"{number} is a Negative Number")
else:
    print("The number is Zero")
