import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class StackProblem {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Stack<Character>> arr = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            arr.add(new Stack<Character>());
        }

        while (sc.hasNext()) {
            String input = sc.next();
            for (Stack<Character> i: arr) {
                i.clear();
            }
            //Complete the code
            try {
                for (int i = 0; i < input.length(); i++) {
                    char c = input.charAt(i);
                    switch (c) {
                        case '{':
                            arr.get(0).push(c);
                            break;
                        case '[':
                            arr.get(1).push(c);
                            break;
                        case '(':
                            arr.get(2).push(c);
                            break;
                        case ')':
                            arr.get(2).pop();
                            break;
                        case '}':
                            arr.get(0).pop();
                            break;
                        case ']':
                            arr.get(1).pop();
                            break;
                    }
                }
                if (arr.get(0).empty() && arr.get(1).empty() && arr.get(2).empty()) {
                    System.out.println("true");
                }
                else {
                    System.out.println("false");
                }
            } catch (Exception e) {
                System.out.println("false");
            }
        }
    }
}
