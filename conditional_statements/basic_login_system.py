username = "admin"
password = "1234"

u = input("Enter Usename: ")
p = input("Enter Passward: ")

if u == username and p == password:
    print("Login Successful!")
elif u == username:
    print("Incorrect Password.")
else:
    print("User not found.")
