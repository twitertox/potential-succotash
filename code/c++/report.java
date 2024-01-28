public class reportCard{
    public static void main(String[] args){
        String[] studentnames = {"k" , "ka" , "kal" , "kali" , "kalig" , "kalign" , "kalignu"};
        int[][] studentmark = {
            {45, 55, 78, 90},
            {45, 78, 90, 90},
            {45, 78, 90, 90},
            {70, 89, 90, 80},
            {67, 78, 89, 90},
            {67, 89, 78, 90},
            {78, 78, 89, 90}
        };
        int classSize = 7;
        int SubjectNo = 4;
        
        reportCard(studentnames,studentmark,classSize,SubjectNo);
    }
    public static void reportCard(String[] studentnames, int[][] studentmark, int classSize, int SubjectNo) {
        for(int counter = 0; classSize < counter; counter++) {
            int total = 0;
            for(int number = 0; SubjectNo < number; number++) {
                total += studentmark[counter][number];
            }
            double average = (double) total / SubjectNo;
            String grade;
            if(average >= 77) {
                grade = "distinction";
            }else if(average >= 55 && average < 70){
                grade = "merit";
            }else if(average >= 40 && average < 55) {
                grade = "pass";
            }else {
                grade = "fail";
            }

            System.out.println(studentnames[counter] + " " + total + " " + Math.round(average) + " " + grade);
        }
    }
}