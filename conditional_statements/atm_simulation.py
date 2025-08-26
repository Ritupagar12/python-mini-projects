balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance and withdraw > 0:
    balance = balance - withdraw
    print("Transaction successful! Remaning balance: ", balance)
elif withdraw <= 0:
    print("Invalid withdrawal amount.")
else:
    print("Insufficiant balance!")
