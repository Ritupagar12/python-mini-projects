import mymodule

print("Module Name: ", mymodule.__name__)
print("Module Doc: ", mymodule.__doc__)
print("Module File: ", mymodule.__file__)

print("Available: ", dir(mymodule))

print(mymodule.greet("Ritu"))
print("Sum: ", mymodule.add(5, 7))
