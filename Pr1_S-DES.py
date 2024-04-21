from Crypto.Cipher import DES

# Pad or truncate the plaintext to a multiple of 8 bytes (DES block size)
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

# Encrypt plaintext using S-DES
def sdes_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = pad(plaintext)
    return cipher.encrypt(plaintext)

# Decrypt ciphertext using S-DES
def sdes_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip()  # Remove padding

# Example usage:
plaintext = b'Hello World!'
key = b'01234567'  # 8-byte key (64 bits)

# Encryption
encrypted = sdes_encrypt(plaintext, key)
print("Encrypted:", encrypted)

# Decryption
decrypted = sdes_decrypt(encrypted, key)
print("Decrypted:", decrypted.decode())
