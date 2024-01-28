StudentName= ["k","ka","kal","kali","kalig","kalign","kalignu"];
StudentMark= [[45,55,78,90],[45,78,90,90],[45,78,90,90],[70,89,90,80],[67,78,89,90],[67,89,78,90],[78,78,89,90]];
ClassSize= 7;
SubjectNo= 4;
def report_card():
    for counter in range(ClassSize):
        total = 0
        for number in range(SubjectNo):
            total = total + StudentMark[counter][number];
        average = total / SubjectNo 
        if average >= 70 :
            grade = "distiction"
        elif average >= 55 or average <= 70 :
            grade = "merit"
        elif average >= 40 or average <= 55:
            grade = "pass"
        elif average < 40 or average > 0:
            grade = "fail"
        print(StudentName[counter],total,round(average,0),grade);
report_card()

