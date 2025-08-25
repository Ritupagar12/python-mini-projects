# Number Range Printer
start = int(input("Enter Start: "))
stop = int(input("Emter Stop: "))
step = int(input("Enter Step: "))

print(f"Numbers from {start} to {stop} with step {step}: ")
for i  in range(start, stop, step):
    print(i)
