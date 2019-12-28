import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SubArraysProblem {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> al = new ArrayList<>();
        int negativeSubArrays = 0;
        for (int i = 0; i < n; i++) {
            al.add(sc.nextInt());
        }

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if(getSumOfSubArray(getSubArray(al, i, j)) < 0){
                    negativeSubArrays++;
                }
            }
        }
        System.out.println(negativeSubArrays);
    }

    private static List<Integer> getSubArray(ArrayList<Integer> al, int start, int end) {
        return al.subList(start, end+1);
    }

    private static int getSumOfSubArray(List<Integer> l) {
        int sum = 0;
        for (Integer i : l) {sum += i;}
        return sum;
    }
}
