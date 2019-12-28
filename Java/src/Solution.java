import java.util.*;

public class Solution {
    static boolean isAnagram(String a, String b) {
        // Complete the function
        HashMap<Character, Integer> h = new HashMap<Character, Integer>();
        HashMap<Character, Integer> h1 = new HashMap<Character, Integer>();
        for (char c: a.toLowerCase().toCharArray()
        ) {
            int num = h.get(c) == null ? 1 : h.get(c) + 1;
            h.put(c, num);
        }
        for (char c: b.toLowerCase().toCharArray()
        ) {
            int num = h1.get(c) == null ? 1 : h1.get(c) + 1;
            h1.put(c, num);
        }
        return h.equals(h1);
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
        ArrayList<Integer> l = new ArrayList<Integer>();
        for (int i=0; i<10; i++) l.add(i);
        Iterator it = l.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
    }
}
