import random

def word_guessing_game():
    words = ["apple", "banana", "chocolate", "elephant", "giraffe", "programming", "computer", "sunshine", "keyboard"]

    # Select a random word from the list
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6  # Number of attempts allowed

    print("Welcome to the Word Guessing Game!")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("Guess a letter or the whole word: ").lower()

        if guess == word_to_guess:
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
        elif len(guess) == 1 and guess.isalpha():
            if guess in word_to_guess:
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        guessed_word[i] = guess
                print(" ".join(guessed_word))
                if "_" not in guessed_word:
                    print("Congratulations! You've guessed the word.")
                    break
            else:
                attempts -= 1
                print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")
        else:
            print("Invalid input. Please enter a single letter or the whole word.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    word_guessing_game()