import javafx.util.Pair;

import java.util.HashSet;
import java.util.Scanner;

public class HashSetProblem {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        HashSet<Pair<String, String>> hs = new HashSet<>();
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];

        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
        for (int i = 0; i < t; i++) {
            Pair<String, String> p = new Pair<>(pair_left[i], pair_right[i]);
            hs.add(p);
        }
        System.out.println(hs.size());
    }
}
