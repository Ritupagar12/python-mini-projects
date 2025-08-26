cart = []

prices = {"apple":2, "banana":1, "milk":3}

while True:
    print("\nShopping Cart: ", cart)
    print("1. Add Items")
    print("2. Checkout")
    choice = input("Choose Option: ")

    if choice == "1":
        item = input("Enter item: ")
        if item in prices:
            cart.append(item)
        else:
            print("Item not available")
    elif choice == "2":
        total = sum(prices[i] for i in cart)
        print("Total Bill = $", total)
        break
    
