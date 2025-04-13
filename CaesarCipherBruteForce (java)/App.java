public class App {
    public static void main(String[] args) {
        CaesarCipherBruteForce cipher = new CaesarCipherBruteForce();

        String message = "LEARNING IS THE BEDROCK OF AI";
        String encrypted = cipher.encrypt(message, 3);

        System.out.println("Encrypted: " + encrypted);
        System.out.println("\nBrute Force Results:");
        cipher.crack(encrypted);
    }
}
