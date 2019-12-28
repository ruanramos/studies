import java.math.BigInteger;
import java.util.Scanner;

public class PrimalityProblemClass {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String n = scanner.nextLine();
        BigInteger num = new BigInteger(n);
        if (num.isProbablePrime(1)) {
            System.out.println("prime");
        } else {
            System.out.println("not prime");
        }
        scanner.close();
    }
}
