import java.math.BigInteger;
import java.util.Scanner;

public class BigIntegers_problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger a = new BigInteger(sc.next());
        sc.next();
        BigInteger b = new BigInteger(sc.next());
        BigInteger sum = a.add(b);
        System.out.println(sum);
        BigInteger mult = a.multiply(b);
        System.out.println(a.multiply(b));


    }
}
