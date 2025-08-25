print("=== Math Quiz ===")

score = 0

questions = [
    {"question": "5 + 3 = ?", "answer": 8},
    {"question": "10 - 4 = ?", "answer": 6},
    {"question": "2 * 6 = ?", "answer": 12},
    {"question": "12 / 4 = ?", "answer": 3.0}
]

for q in questions:
    user_answer = float(input(q["question"] + " "))
    if user_answer == q["answer"]:
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}")

print(f"\nYour Final score: {score}/{len(questions)}")
        
