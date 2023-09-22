import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_game():
    print("Welcome to the Dice Rolling Game!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled: {result}")
        if result == 6:
            print("Congratulations, you rolled a 6 and won!")
        else:
            print("Sorry, you didn't roll a 6. Try again!")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_dice_game()