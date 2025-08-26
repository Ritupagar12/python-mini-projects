users = ["john", "bob", "alice"]

username = input("Enter username: ")
if username in users:
    print("Access Granted")
else:
    print("Access Denied")
