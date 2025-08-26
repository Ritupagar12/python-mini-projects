#Assigns grades (A-F) based on marks.

marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "F"

print("Your grade is ", grade)
