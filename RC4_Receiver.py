from Crypto.Cipher import ARC4

def receiver():
    
    with open('encrypted_message.bin', 'rb') as f:
        ciphertext = f.read()

    
    key = input("Enter the secret key (password) used for encryption: ").encode()

  
    cipher = ARC4.new(key)

    
    plaintext = cipher.decrypt(ciphertext)

    print("Decrypted message:", plaintext.decode())

if __name__ == "__main__":
    receiver()
