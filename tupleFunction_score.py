def main():
    Scores = Read_Scores()
    Grades = checkGrade(Scores)
    Report(Scores, Grades)
    print(f'End Program\n')


def Read_Scores():
    Scores = ()
    count = 1
    loop = True
    
    while loop:
        score = int(input(f'Enter score #{count} (-1 to Exit) : '))
        if (score >= 0) and (score <= 100):
            Scores += (score, )
            count += 1
        elif score == -1:
            loop = False
    count -= 1
    return(Scores)


def checkGrade(Scores):
    Grades = ()
    for score in Scores:
        grade = ''
        if score >= 80:
            grade = 'A'
        elif score >= 70:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        elif score >= 50:
            grade = 'D'
        else:
            grade = 'F'
        Grades += (grade, )
    return(Grades)


def Report(Scores, Grades):
    Max = len(Scores)
    print()
    print('='*24)
    print('| No. | Scores | Grade |')
    print('='*24)
    for i in range(Max):
        print(f'| %2d  |   %3d  |   %s   |' %(i+1, Scores[i], Grades[i]))
    print('='*24)


main()