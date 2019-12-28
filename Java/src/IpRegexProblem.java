import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class IpRegexProblem{

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}

//Write your code here
class MyRegex {
    private String piece = "[0-2][0-5][0-5]|[0-5]]";
    String pattern = piece + "." + piece + "." + piece + "." + piece;
}