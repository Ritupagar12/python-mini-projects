def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Unit Converter")
print("1. km -> Miles")
print("2. miles -> km")
print("3. Celsius -> Fahrenheit")
print("4. Fahrenheit -> Celsius")

choice = int(input("Choose conversion (1-4): "))

if choice == 1:
    km = float(input("Enter km: "))
    print("Miles = ", km_to_miles(km))
elif choice == 2:
    miles = float(input("Enter miles: "))
    print("Km = ", miles_to_km(miles))
elif choice == 3:
    celsius = float(input("Enter Celsius: "))
    print("Fahrenheit = ", celsius_to_fahrenheit(celsius))
elif choice == 4:
    fahrenheit = float(input("Enter Fahrenheit: "))
    print("Celsius = ", fahrenheit_to_celsius(fahrenheit))
else:
    print("Invalid Choice")
