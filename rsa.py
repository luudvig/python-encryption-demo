#!/usr/bin/env python3

# Hard-coded prime numbers p and q (not secure in practice)
p = 53
q = 59

# Compute n (modulus)
n = p * q

# Compute the totient (phi)
phi = (p - 1) * (q - 1)

# Choose e (public exponent)
e = 65537

# Calculate d (private exponent)
d = pow(e, -1, phi)

# Message to be encrypted and decrypted
message_str = "Hello, RSA Encryption!"
message_bytes = message_str.encode('utf-8')

# Encryption
cipher = [pow(b, e, n) for b in message_bytes]

# Decryption
decrypted_message_bytes = bytes([pow(c, d, n) for c in cipher])
decrypted_message_str = decrypted_message_bytes.decode('utf-8')

print("Original Message:", message_str)
print("Encrypted Message (Cipher):", cipher)
print("Decrypted Message:", decrypted_message_str)
