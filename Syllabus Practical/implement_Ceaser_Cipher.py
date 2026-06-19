def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)



text = input("Enter Plain Text: ")
shift = int(input("Enter Shift Value: "))

# Encryption
cipher = caesar_encrypt(text, shift)
print("Encrypted Text:", cipher)

# Decryption
plain = caesar_decrypt(cipher, shift)
print("Decrypted Text:", plain)
