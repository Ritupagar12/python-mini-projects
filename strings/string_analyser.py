text = input("Enter a string: ")

print("\nString Analysis:")
print("Original String: ", text)
print("Length: ", len(text))
print("Uppercase: ", text.upper())
print("Lowercase: ", text.lower())
print("Title Case: ", text.title())
print("Reversed String: ", text[::-1])

char = input("Enter a character to count: ")
print(f"The character '{char}' appears {text.count(char)} time.")

letter = input("Enter a letter to check membership: ")
print(f"Is '{letter}' in the string? {'Yes' if letter in text else 'No'}")
