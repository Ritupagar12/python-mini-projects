tasks = []

while True:
    print("\nTo-Do List:", tasks)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found!")
    elif choice == "3":
        break
