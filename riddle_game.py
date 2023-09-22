def riddle_game():
    print("Welcome to the Riddle Game!")

    riddles = [
        {"question": "I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?", "answer": "fire"},
        {"question": "I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "answer": "fire"},
        {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo"}
    ]

    for i, riddle in enumerate(riddles, start=1):
        print(f"\nRiddle {i}:\n{riddle['question']}\n")

    correct_answer = riddle["answer"]
    attempts = 3

    while attempts > 0:
        guess = input("Your answer: ").strip().lower()

        if guess == correct_answer:
            print("Congratulations! You've solved the riddle.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Sorry, that's not correct. You have {attempts} attempts left.")
            else:
                print("You've run out of attempts. The answer was '{correct_answer}'.")
                break

if __name__ == "__main__":
    riddle_game()