data = list(map(int, input("Enter integers: ").split()))
squares_of_evens = list(map(lambda n: n* n, filter(lambda n: n%2==0, data)))
print("Square of evens:", squares_of_evens)
    
