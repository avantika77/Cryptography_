# we need  the alphabet b/c we convert letters into numericals values
# to be able to use the mathematical operation [spaces also]
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
KEY = 3


def caesar_encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()  # Convert to uppercase
    # convert the plain text into upper case letters
    # c='E'
    # find the numerical representation (index) associated with the letter
# consider all the letter in the plain text and convert them into their numerical values
    for c in plain_text:
        index = ALPHABET.find(c)
        if index != -1:  # Only encrypt characters that exist in ALPHABET
            index = (index + KEY) % len(ALPHABET)
            # the range [0,num_of_letters _in the alphabet]
            cipher_text += ALPHABET[index]
        else:
            # Keep unknown characters as is (e.g., numbers, punctuation)
            cipher_text += c

    return cipher_text
plain_text = input("Enter text to encrypt: ")
encrypted_text = caesar_encrypt(plain_text)
print("Encrypted:", encrypted_text)
