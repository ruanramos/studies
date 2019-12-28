import java.util.BitSet;
import java.util.Scanner;
import java.lang.reflect.*;

public class BitSetProblem {
    public static void main(String[] args) throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        Scanner sc = new Scanner(System.in);

        int lenBitSets = sc.nextInt();
        BitSet bs1 = new BitSet(lenBitSets);
        BitSet bs2 = new BitSet(lenBitSets);
        int numOperations = sc.nextInt();

        for (int i = 0; i < numOperations; i++) {
            String operation = sc.next();
            Method method;
            switch (operation) {
                case "AND":
                case "OR":
                case "XOR":
                    method = bs1.getClass().getMethod(operation.toLowerCase(), BitSet.class);
                    int set1 = sc.nextInt();
                    int set2 = sc.nextInt();
                    if (set1 == 1) {
                        method.invoke(bs1, bs2);
                    } else if (set2 == 1) {
                        method.invoke(bs2, bs1);
                    }
                    break;
                case "SET":
                case "FLIP":
                    method = bs1.getClass().getMethod(operation.toLowerCase(), int.class);
                    int set = sc.nextInt();
                    int index = sc.nextInt();
                    if (set == 1) {
                        method.invoke(bs1, index);
                    } else if (set == 2) {
                        method.invoke(bs2, index);
                    }
                    break;
            }
            System.out.println(bs1.cardinality() + " " + bs2.cardinality());
        }
    }
}
