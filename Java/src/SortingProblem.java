import java.util.*;

class Student {
    private int id;
    private String fname;
    private double cgpa;

    Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }

    public int getId() {
        return id;
    }

    String getFname() {
        return fname;
    }

    public double getCgpa() {
        return cgpa;
    }
}

class StudentSort implements Comparator {

    @Override
    public int compare(Object o1, Object o2) {
        Student s1 = (Student) o1;
        Student s2 = (Student) o2;
        if (s1.getCgpa() < s2.getCgpa()) return 1;
        if (s1.getCgpa() > s2.getCgpa()) return -11;
        if (s1.getFname().compareTo(s2.getFname()) < 0) return -1;
        if (s1.getFname().compareTo(s2.getFname()) > 0) return 1;
        return Integer.compare(s1.getId(), s2.getId());
    }
}

//Complete the code
public class SortingProblem {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<Student>();
        while (testCases > 0) {
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            Student st = new Student(id, fname, cgpa);
            studentList.add(st);

            testCases--;
        }

        StudentSort ss = new StudentSort();
        studentList.sort(ss);

        for (Student st : studentList) {
            System.out.println(st.getFname());
        }
    }
}




