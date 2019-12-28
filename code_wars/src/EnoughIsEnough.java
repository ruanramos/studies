import java.util.HashMap;
import java.util.Map;

public class EnoughIsEnough {

    public static int[] deleteNth(int[] elements, int maxOccurrences) {
        //Code here ;)
        Map m = new HashMap<Integer, Integer>();
        for (int element : elements) {
            m.merge(element, 1, { a, b -> a + b});
        }
    }

}