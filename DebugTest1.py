def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            shift = 65 if char.isupper() else 97
            if key > 0:
                encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            else:
                encrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            result += encrypted_char
    return result

def main():
    user_input = input("Enter the text to encrypt: ")
    key = int(input("Enter the encryption key (positive for encryption, negative for decryption): "))

    encrypted_text = caesar_cipher(user_input, key)

    if key > 0:
        print("Encrypted text:", encrypted_text)
    else:
        decrypted_text = caesar_cipher(encrypted_text, key)
        print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()