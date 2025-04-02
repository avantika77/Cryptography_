def caesar_decrypt(cipher_text, key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabacdefghijklmnopqrstuvwxyz "): #key to shift the letter by key positions
    decrypted_text = "" #store the final decrypted message.
    cipher_text = cipher_text.upper()
    for i in cipher_text:
        if i in alphabet:
            index = alphabet.find(i)
            new_index = (index - key) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += i  # Preserve non-alphabet characters
    return decrypted_text  
# Take input from user
cipher_text = input("Enter the encrypted text: ")
key = int(input("Enter the shift key: "))
# Decrypt and result
decrypted_text = caesar_decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)
