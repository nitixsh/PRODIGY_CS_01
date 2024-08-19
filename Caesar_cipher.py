# Q.1. Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
# Allow users to input a message and a shift value to perform encryption and decryption.

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabetic characters as they are
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice in ['E', 'D']:
            text = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'E':
                encrypted_text = caesar_cipher(text, shift, mode='encrypt')
                print("Encrypted message:", encrypted_text)
            elif choice == 'D':
                decrypted_text = caesar_cipher(text, shift, mode='decrypt')
                print("Decrypted message:", decrypted_text)
        else:
            print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
        
        another = input("Do you want to process another message? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()