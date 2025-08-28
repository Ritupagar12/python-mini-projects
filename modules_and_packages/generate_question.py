import random

def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = a+ b
    user = int(input(f"What is {a} + {b}? "))
    if user == answer:
        print("Correct!")
    else:
        print("Wrong! The answer is ", answer)

generate_question()
