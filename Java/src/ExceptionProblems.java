import java.util.Scanner;

class MyCalculator {
    /*
     * Create the method long power(int, int) here.
     */
    long power(int n, int p) throws Exception {
        if (n < 0 | p < 0) {
            throw new Exception("n or p should not be negative.");
        } else if (n == 0 | p == 0) {
            throw new Exception("n and p should not be zero.");
        }
        return (long) Math.pow((double) n, (double) p);
    }

}

public class ExceptionProblems {
    /*
    public static void main(String[] args) {
        int x, y;
        Scanner s = new Scanner(System.in);
        try {
            x = s.nextInt();
            y = s.nextInt();
            System.out.println(x/y);
        } catch (InputMismatchException e1) {
            System.out.println(e1.toString().substring(0, 32));
        } catch (ArithmeticException e2) {
            System.out.println(e2);
        }
    }
     */
    public static final MyCalculator my_calculator = new MyCalculator();
    public static final Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        while (in.hasNextInt()) {
            int n = in.nextInt();
            int p = in.nextInt();

            try {
                System.out.println(my_calculator.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}
