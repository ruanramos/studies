import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.util.function.IntFunction;
import java.util.regex.*;
import java.security.*;


public class Solution1 {

    public static void main(String[] args) throws Exception {
        DoNotTerminate.forbidExit();

        IntFunction<Boolean> a1 = (int n) -> n == 10;
        System.out.println(a1);

        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int num = Integer.parseInt(br.readLine().trim());
            Object o;// Must be used to hold the reference of the instance of the class Solution.Inner.Private

            //Write your code here
            Inner i = new Inner();
            o = i.new Private();
            ((Inner.Private)o).powerof2(num);
            System.out.println("An instance of class: " + o.getClass().getCanonicalName() + " has been created");

        }//end of try

        catch (DoNotTerminate.ExitTrappedException e) {
            System.out.println("Unsuccessful Termination!!");
        }
    }//end of main
    static class Inner{
        private class Private{
            private String powerof2(int num){
                return ((num&num-1)==0)?"power of 2":"not a power of 2";
            }
        }
    }//end of Inner

}//end of Solution

