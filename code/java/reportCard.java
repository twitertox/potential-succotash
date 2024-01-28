public class reportCard{
    public static void main(String[] args) {
        String[] studentName = {"k", "ka", "kal", "kali", "kalig", "kalign", "kalignu"};
        int[][] studentMark = {
                {45, 55, 78, 90},
                {45, 78, 90, 90},
                {45, 78, 90, 90},
                {70, 89, 90, 80},
                {67, 78, 89, 90},
                {67, 89, 78, 90},
                {78, 78, 89, 90}
        };
        int classSize = 7;
        int subjectNo = 4;

        reportCard(studentName, studentMark, classSize, subjectNo);
    }

    public static void reportCard(String[] studentName, int[][] studentMark, int classSize, int subjectNo) {
        for (int counter = 0; counter < classSize; counter++) {
            int total = 0;
            for (int number = 0; number < subjectNo; number++) {
                total += studentMark[counter][number];
            }
            double average = (double) total / subjectNo;
            String grade;

            if (average >= 70) {
                grade = "distinction";
            } else if (average >= 55 && average < 70) {
                grade = "merit";
            } else if (average >= 40 && average < 55) {
                grade = "pass";
            } else {
                grade = "fail";
            }

            System.out.println(studentName[counter] + " " + total + " " + Math.round(average) + " " + grade);
        }
    }
}