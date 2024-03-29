def stream_cipher_encrypt(plaintext, key):
    # Initialize the ciphertext as an empty string
    ciphertext = ""
    # Repeat the key to match the length of the plaintext
    repeated_key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    # Encrypt each character of the plaintext using XOR with the corresponding key character
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(repeated_key[i]))
    return ciphertext

def stream_cipher_decrypt(ciphertext, key):
    # Initialize the plaintext as an empty string
    plaintext = ""
    # Repeat the key to match the length of the ciphertext
    repeated_key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    # Decrypt each character of the ciphertext using XOR with the corresponding key character
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(repeated_key[i]))
    return plaintext

# Example usage
plaintext = "Hello, World!"
key = "secretkey"
encrypted_text = stream_cipher_encrypt(plaintext, key)
decrypted_text = stream_cipher_decrypt(encrypted_text, key)

print("Plain Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
