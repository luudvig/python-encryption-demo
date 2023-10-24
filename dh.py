#!/usr/bin/env python3

# Diffie-Hellman key exchange
p = 23  # Prime number
g = 5   # Generator

# Alice's private key
private_key_alice = 6

# Bob's private key
private_key_bob = 15

# Alice computes her public key
public_key_alice = (g ** private_key_alice) % p

# Bob computes his public key
public_key_bob = (g ** private_key_bob) % p

# Shared secret computation
shared_secret_alice = (public_key_bob ** private_key_alice) % p
shared_secret_bob = (public_key_alice ** private_key_bob) % p

# Message to be encrypted
message = "Hello, Bob!"

# Encryption and decryption using the shared secret
def encrypt(plain_text, shared_secret):
    encrypted = []
    for char in plain_text:
        encrypted_char = chr(ord(char) + shared_secret)
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

def decrypt(cipher_text, shared_secret):
    decrypted = []
    for char in cipher_text:
        decrypted_char = chr(ord(char) - shared_secret)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

# Alice encrypts the message with the shared secret
encrypted_message = encrypt(message, shared_secret_alice)

# Bob decrypts the message with the shared secret
decrypted_message = decrypt(encrypted_message, shared_secret_bob)

print(f"Alice's original message: {message}")
print(f"Encrypted Message (Cipher): {encrypted_message}")
print(f"Bob decrypted the message: {decrypted_message}")
