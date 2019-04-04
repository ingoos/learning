score = [100, 55, 70 ,35 , 90]
for number in range(len(score)):
    if((score[number]) >= 60):
        print("%d 학생 합격" % (number+1)) 
    else:
        print("%d 학생 불합격" % (number+1))
