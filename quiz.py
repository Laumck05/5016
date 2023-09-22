# Define a list of quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Giraffe", "Elephant", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    }
]

# Initialize the user's score
score = 0

# Iterate through the quiz questions
for i, question in enumerate(questions, start=1):
    print(f"Question {i}: {question['question']}")
    for j, option in enumerate(question["options"], start=1):
        print(f"{j}. {option}")
    
    # Get the user's answer
    user_answer = input("Enter the number of your answer: ")
    
    # Check if the user's answer is correct
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["options"]):
        if question["options"][int(user_answer) - 1] == question["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['correct_answer']}\n")
    else:
        print("Invalid input. Skipping to the next question.\n")

# Display the user's final score
print(f"Your Score: {score}/{len(questions)}")