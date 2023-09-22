# Function to encrypt a message using a Caesar cipher
def encrypt_message(message, key):
    encrypted_message = ""

    for char in message:
        # Check if the character is alphabetical
        if char.isalpha():
            # Determine whether to shift forward or backward based on the key
            shift = key % 26  # Ensure the shift is within the range of the alphabet
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # If the character is not alphabetical, keep it unchanged
            encrypted_char = char

        encrypted_message += encrypted_char

    return encrypted_message

while True:
    # Prompt the user for a message and an encryption key
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the encryption key (an integer): "))

    # Encrypt the message
    encrypted_message = encrypt_message(message, key)

    # Output the encrypted message
    print("Encrypted Message:", encrypted_message)

    # Ask the user if they want to encrypt another message or exit
    another_message = input("Encrypt another message? (yes/no): ").strip().lower()
    if another_message != 'yes':
        break