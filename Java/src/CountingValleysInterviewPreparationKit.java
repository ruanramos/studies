import java.io.*;
        import java.math.*;
        import java.security.*;
        import java.text.*;
        import java.util.*;
        import java.util.concurrent.*;
        import java.util.regex.*;

public class CountingValleysInterviewPreparationKit {

    // Complete the countingValleys function below.
    static int countingValleys(int n, String s) {
        int valleys = 0;
        int counter = 0;
        boolean inValley = false;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == "U".toCharArray()[0]) {
                if (inValley && ++counter == 0) {
                    valleys++;
                    inValley = false;
                }
            }
            if (s.charAt(i) == "D".toCharArray()[0]) {
                if (!inValley && --counter < 0) {
                    inValley = true;
                }
            }
        }
        return valleys;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();

        int result = countingValleys(n, s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
