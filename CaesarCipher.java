package com.globalsoftwaresupport;
public class CaesarCipher {
    //26alphabet
    private String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public String encrypt(String plaintext, int key) {
        String cipherText = "";
        plaintext = plaintext.toUpperCase();

        //consider all the letters in the plain_text
        for (int i = 0; i < plaintext.length(); i++) {
            char character = plaintext.charAt(i);
            int charIndex = ALPHABET.indexOf(character);
       //Caser  encrption is just a simple shift of characters according to the key 
       //use modular airthmetic to transform the values within  the range 
       // [0,num_of_letters_in_alphabet]
       if (charIndex != -1) {
       int encryptionIndex=(CharIndex+key)%ALPHABET.lenght();
       //keep appending the encrypted character to the cipher_text
       cipherText+=ALPHABET.charAt(encryptedIndex);
        }else{
            cipherText+=character;
        }
        return cipherText;
    }
    public String decrypt(String cipherText, int key){
        String plainText="";
        for (int i=i<cipherText.length(); i++){
            char character=cipherText.charAt(i);
            int charIndex=ALPHABET.indexOf(character);
            int decryptionIndex= ChartAt(decryption);
            plainText +=ALPHABET.chatAt(decryption);
            }
        }
    }
    }


