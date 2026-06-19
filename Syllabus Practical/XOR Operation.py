
text = "Hello World"

# XOR each character with 0
result = ""

for ch in text:
    result += chr(ord(ch) ^ 0)

print("Original String:", text)
print("Result after XOR with 0:", result)
