price_per_donut= 105.50
quantity = 36
amount = price_per_donut * quantity

if amount > 10000:
    discount = amount * 0.10
    amount=amount-discount
elif amount > 5000:
    discount = amount * 0.05
    amount=amount-discount
elif amount > 2000:
    discount = amount * 0.02
    amount=amount-discount
elif amount > 1000:
    discount = amount * 0.01
    amount=amount-discount
else:
    print("No discount applicable.")

print("Amount Payable: ", amount)
