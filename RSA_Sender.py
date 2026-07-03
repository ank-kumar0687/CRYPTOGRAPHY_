from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

def sender():
    try:
       
        with open('receiver_public.pem', 'rb') as f:
            receiver_public_key = serialization.load_pem_public_key(f.read())
    except FileNotFoundError:
        print("Error: 'receiver_public.pem' file not found. Run key generation first.")
        return

    
    message = input("Enter the message to encrypt and send: ").encode()

    try:
        
        ciphertext = receiver_public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        
        with open('encrypted_message.bin', 'wb') as f:
            f.write(ciphertext)

        print("✅ Message encrypted and saved as 'encrypted_message.bin'.")
    except Exception as e:
        print("❌ Encryption failed:", str(e))

if __name__ == "__main__":
    sender()
