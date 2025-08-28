def is_palindrome(word):
    return word == word[::-1]

w = input("Enter a word: ")
if is_palindrome(w):
    print(w, "is a palindrome")
else:
    print(w, "is not a palindrome")
