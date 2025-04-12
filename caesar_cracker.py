# We need the alphabet because we convert letters into numerical values
# to be able to use mathematical operations (note we encrypt spaces as well)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

def crack_caesar(cipher_text):
       # Try all possible keys
    for key in range(len(ALPHABET)):
             # EMPTY STRING
        plain_text = ''
            # simple caesar cipher decryption algorithm
 
        for c in cipher_text.upper():
            if c in ALPHABET:
                index = ALPHABET.find(c)
                index = (index - key) % len(ALPHABET)
                plain_text += ALPHABET[index]
            else:
                plain_text += c
                # PRINT THE actual decrypted string with given key
        print(f'With key {key}, the result is: {plain_text}')

if __name__ == '__main__':
    encrypted = 'MJQQT BTWQI YMNX NX F XJHWJY RJXXFLJ'
# Encrypted message in uppercase
    crack_caesar(encrypted)

#With key 5, the result is: HELLOVXORLDVTHISVISVAVSECRETVMESSAGE (answer)