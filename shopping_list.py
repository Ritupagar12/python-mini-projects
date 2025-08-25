#Shopping List Manager
print("=== Shopping List Manager ===")

shopping_list = []

while True:
    item = input("Enter item to add (or 'done' to finish): ").strip()
    if item.lower() == "done":
        break
    shopping_list.append(item)

#Remove duplicates using set
unique_items = list(set(shopping_list))

#Check if an item exists
check_item = input("Check if an item exists in your list: ")
exists = check_item in unique_items

print("\n--- Your Shopping List ---")
for i, item in enumerate(unique_items, 1):
    print(f"{i}.{item}")

print(f"\nDoes '{check_item}' exist in your lists? {exists}")
