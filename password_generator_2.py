import random
import string

def generate_random_password(length, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random Password Generator")
    
    while True:
        length = int(input("Enter the desired password length: "))
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_random_password(length, use_digits, use_special_chars)
        print(f"Generated Password: {password}")

        another_password = input("Generate another password? (yes/no): ").lower()
        if another_password != 'yes':
            break
