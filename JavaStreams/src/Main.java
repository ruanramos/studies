import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        FilesManager a = new FilesManager();
        //File f = a.CreateFile("File_Test_Once_Again");


        List<Integer> l = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            int finalI = i;
            (int p) -> {return finalI * finalI; };
        }


    }

    public static class FilesManager {
        public File CreateFile(String name) throws FileNotFoundException, IOException {
            Scanner sc = new Scanner(System.in);
            File f = new File(name + ".txt");
            OutputStream os = null;
            try {
                os = new FileOutputStream(f);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            String line = sc.nextLine();
            while (!line.equals("q")) {
                try {
                    assert os != null;
                    os.write(line.getBytes());
                    os.write("\n".getBytes());
                } catch (IOException e) {
                    e.printStackTrace();
                }
                line = sc.nextLine();
            }
            try {
                assert os != null;
                os.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return f;
        }


    }
}
