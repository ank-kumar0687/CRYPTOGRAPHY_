def rail_fence_encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    result = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


# Main Program
plaintext = input("Enter Plain Text: ")
key = int(input("Enter Number of Rails: "))

ciphertext = rail_fence_encrypt(plaintext, key)

print("Encrypted Text:", ciphertext)
