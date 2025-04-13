public class CaesarCipherBruteForce {

    private final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Encrypts the given plain text with a Caesar cipher shift
    public String encrypt(String plainText, int shift) {
        plainText = plainText.toUpperCase();
        StringBuilder cipherText = new StringBuilder();

        for (char character : plainText.toCharArray()) {
            if (ALPHABET.indexOf(character) != -1) {
                int charIndex = ALPHABET.indexOf(character);
                int encryptedIndex = (charIndex + shift) % ALPHABET.length();
                cipherText.append(ALPHABET.charAt(encryptedIndex));
            } else {
                cipherText.append(character); // Non-alphabet characters remain unchanged
            }
        }

        return cipherText.toString();
    }

    // Brute-force method to try all possible shifts
    public void crack(String cipherText) {
        cipherText = cipherText.toUpperCase();

        for (int key = 0; key < ALPHABET.length(); key++) {
            StringBuilder plainText = new StringBuilder();

            for (int i = 0; i < cipherText.length(); i++) {
                char character = cipherText.charAt(i);

                if (ALPHABET.indexOf(character) != -1) {
                    int charIndex = ALPHABET.indexOf(character);
                    int decryptedIndex = Math.floorMod(charIndex - key, ALPHABET.length());
                    plainText.append(ALPHABET.charAt(decryptedIndex));
                } else {
                    plainText.append(character);
                }
            }

            System.out.println("Key " + key + ": " + plainText);
        }
    }
}
