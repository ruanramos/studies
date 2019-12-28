import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numArrays = sc.nextInt();
        ArrayList<ArrayList<Integer>> al = new ArrayList<>();
        for (int i=0; i < numArrays; i++) {
            int numElements = sc.nextInt();
            ArrayList<Integer> internAl = new ArrayList<Integer>();
            for (int j=0; j<numElements; j++) {
                internAl.add(sc.nextInt());
            }
            al.add(internAl);
        }
        int numQueries = sc.nextInt();
        for (int i = 0; i < numQueries; i++) {
            try {
                al.get(sc.nextInt() - 1).get(sc.nextInt() - 1);
            } catch (Exception e) {
                System.out.println("ERROR!");
            }

        }
    }
}
