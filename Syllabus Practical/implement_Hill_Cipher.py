def hill_cipher_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")

    
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    cipher_text = ""

    for i in range(0, len(plaintext), 2):
        p1 = ord(plaintext[i]) - ord('A')
        p2 = ord(plaintext[i + 1]) - ord('A')

        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        cipher_text += chr(c1 + ord('A'))
        cipher_text += chr(c2 + ord('A'))

    return cipher_text


# 2x2 Key Matrix
key = [[3, 3],
       [2, 5]]

plaintext = input("Enter Plain Text: ")

cipher = hill_cipher_encrypt(plaintext, key)

print("Encrypted Text:", cipher)
