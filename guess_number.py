import random

number = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")

    if not guess.isdigit():
        print("Invalid Input! Enter a number: ")
        continue

    guess = int(guess)

    if guess == number:
        print("Correct! You guessed it!")
        break
    elif guess < number:
        print("Too Low, try again.")
    else:
        print("Too High, try again.")
