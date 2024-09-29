def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher with the given shift."""
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
    return result

def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher with the given shift."""
    return encrypt(text, -shift)  # Reuse the encrypt function with negative shift for decryption

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
