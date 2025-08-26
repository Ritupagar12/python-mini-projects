grades = {}

while True:
    print("\nGradebook: ", grades)
    print("1. Add/Update Grade")
    print("2. View Grade")
    print("3. Exit")
    choice = input("Choose Option: ")

    if choice == "1":
        name = input("Enter Student Name:")
        grade = input("Enter Grade:")
        grades[name] = grade
    elif choice == "2":
        name = input("Enter Student Name: ")
        print("Grade: ", grades.get(name, "Not found"))
    elif choice == "3":
        break
