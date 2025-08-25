import random

print("Welcome to the Number Guessing Game!")

#Computer picks a number 1-10.
secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Correct! You guessed it!")
        break
    elif guess < secret:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

