contacts = {}

while True:
    print("\nContacts: ", contacts)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")
    choice = input("Choose Option:")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter name: ")
        print("Phone: ", contacts.get(name, "Not Found"))
    elif choice == "3":
        break
