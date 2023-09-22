import random
import string

def generate_random_password ():
    # Define charactors  for password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Password length
    password_length = 8
    #Generate random password
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password 

def main ():
    while True:
        print("Request Password Change")
        print("0. Request password change")
        print("1. Quit")

        choice = input("Enter 0 to request a password change or 1 to quit: ")

        if choice == '0':
            new_password = generate_random_password()
            print(f"Your new password is: {new_password}")
        elif choice == '1':
            print("Thank You")
            break
        else:
            print("Invalid choice. Please select 0 to request a new password or 1 to quit.")

if __name__ == "__main__":
    main()
