products = [
    {"sku": "P1", "name": "pen", "price": 1.5},
    {"sku": "P2", "name": "book", "price": 4.0},
    {"sku": "P3", "name": "eraser", "price": 0.5}
]

mode = input("Sort by name/price? ").strip().lower()
key = (lambda x: x["name"]) if mode == "name" else (lambda x: x["price"])
for p in sorted(products, key=key):
    print(p)
