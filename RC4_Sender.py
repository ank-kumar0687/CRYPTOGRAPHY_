from Crypto.Cipher import ARC4

def sender():
   
    plaintext = input("Enter the message: ").encode()

    
    key = input("Enter a secret key (password): ").encode()

   
    cipher = ARC4.new(key)

    
    ciphertext = cipher.encrypt(plaintext)

  
    with open('encrypted_message.bin', 'wb') as f:
        f.write(ciphertext)

    print("Message encrypted and saved as 'encrypted_message.bin'")

if __name__ == "__main__":
    sender()
