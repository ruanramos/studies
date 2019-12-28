import java.util.HashMap;

public class Strings_testing {
    public static void main(String[] args) {

        /*
        String s = "welcometojava";
        int k = 3;

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        System.out.println(A.length() + B.length());
        String res = A.compareTo(B) > 0 ? "Yes" : "No";
        System.out.println(res);
        System.out.printf("%s %s", A.substring(0,1).toUpperCase() + A.substring(1), B.substring(0,1).toUpperCase() + B.substring(1));


        -----------------------------------------------------------------
        String smallest = s.substring(0, k);
        String largest = "";

        List<String> l = new ArrayList<String>();
        for (int i=0; i <= s.length()-k; i++) {
            String sub = s.substring(i, i+k);
            System.out.println(sub.compareTo(smallest + "-" + sub));
            l.add(sub);
            smallest = sub.compareTo(smallest) > 0 ? smallest : sub;
            largest = sub.compareTo(largest) > 0 ? sub : largest;
        }


        System.out.println(smallest + "\n" + largest);
        System.out.println(l);
        -----------------------------------------------------------------
        Scanner sc=new Scanner(System.in);
        String A=sc.next();

        StringBuilder sb = new StringBuilder(A);
        String res = sb.reverse().toString().equals(A) ? "Yes" : "No";
        System.out.println(res);

        */
        String s = "cachorro";
        String s2 = "crcoahor";
        HashMap<Character, Integer> h = new HashMap<Character, Integer>();
        HashMap<Character, Integer> h1 = new HashMap<Character, Integer>();
        for (char c : s.toCharArray()
        ) {
            int num = h.get(c) == null ? 1 : h.get(c) + 1;
            h.put(c, num);
        }
        for (char c : s2.toCharArray()
        ) {
            int num = h1.get(c) == null ? 1 : h1.get(c) + 1;
            h1.put(c, num);
        }
        System.out.println(h.equals(h1));
    }
}
