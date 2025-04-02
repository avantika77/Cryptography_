# we need  the alphabet b/c we convert letters into numericals values
# to be able to use the mathematical operation [spaces also]
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
KEY = 3

def caesar_encrypt(plain_text, key=KEY):
    cipher_text = ''
    plain_text = plain_text.upper()
    # find the numerical representation (index) associated with the letter
# consider all the letter in the plain text and convert them into their numerical values
    for i in plain_text:
        index = ALPHABET.find(i)
        if index != -1:  # Ensure only valid characters are processed
            index = (index + key) % len(ALPHABET)
            cipher_text += ALPHABET[index]
        else:
            cipher_text += i  # Preserve non-alphabet characters
    
    return cipher_text
#decryption
def caesar_decrypt(cipher_text, key=KEY):
    plain_text = ''
    cipher_text = cipher_text.upper()
    #opposite of encryption
    for j in cipher_text:
        index = ALPHABET.find(j)
        if index != -1:
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]
        else:
            plain_text += j
    
    return plain_text
plain_text = input("Enter text to encrypt: ")
encrypted_text = caesar_encrypt(plain_text)
print("Encrypted:", encrypted_text)
decrypted_text = caesar_decrypt(encrypted_text)
print("Decrypted:", decrypted_text)
