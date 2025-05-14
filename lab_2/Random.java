import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        byte[] bytes = new byte[16];
        random.nextBytes(bytes);
        for (byte b : bytes) {
            for (int i = 7; i >= 0; i--) {
                System.out.print((b >> i) & 1);
            }
        }
    }
}