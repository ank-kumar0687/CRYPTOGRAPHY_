def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result


def encrypt_playfair(text, matrix):
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:  # Same column
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:  # Rectangle rule
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


# Main Program
key = input("Enter Key: ")
plaintext = input("Enter Plain Text: ")

matrix = generate_matrix(key)
prepared_text = prepare_text(plaintext)

print("\nPlayfair Matrix:")
for row in matrix:
    print(row)

ciphertext = encrypt_playfair(prepared_text, matrix)

print("\nPrepared Text:", prepared_text)
print("Encrypted Text:", ciphertext)
