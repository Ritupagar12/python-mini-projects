print("=== Simple Profile Card ===")

#Collect user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

#Store data in a dictionary
profile = {
    "Name": name,
    "Age": age,
    "Height": height
}

#Print formatted card
print("\n--- Profile Card---")
for key, value in profile.items():
    print(f"{key}: {value}")
           
