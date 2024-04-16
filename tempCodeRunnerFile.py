from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
 
def encrypt(plaintext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the plaintext and encrypt it
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext
 
def decrypt(ciphertext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext and remove the padding
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data
 
plaintext = b"This is the message to be encrypted"
key = get_random_bytes(32)  # Generating keys/passphrase
print("Key:", key.hex())
# Encryption
encrypted_data = encrypt(plaintext, key)
print("Encrypted data:", encrypted_data)
# Decryption
decrypted_data = decrypt(encrypted_data, key)
print("Decrypted data:", decrypted_data)
