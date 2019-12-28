import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class ListProblem {

    private static final String INSERT = "Insert";
    private static final String DELETE = "Delete";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> l = new LinkedList<Integer>();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            l.addLast(sc.nextInt());
            //System.out.println(i);
        }
        //printList(l);
        int n1 = sc.nextInt();
        for (int i = 0; i < n1; i++) {
            String operation = sc.nextLine();
            if (operation.length() < 3) operation = sc.nextLine();
            if (operation.equals(INSERT)) {
                l.add(sc.nextInt(), sc.nextInt());
            } else {
                l.remove(sc.nextInt());
            }
        }
        printList(l);
    }
    private static void printList(List<Integer> l) {
        for (Integer i : l) {
            System.out.print("" + i + " ");
        }
    }
}
