def main():
    loop = True
    while loop:
        score = int(input('Enter score (-1 to exit) : '))
        if score>=0 and score <=100:
            grade = checkGrade(score)
            print(f'Score {score}, get grade : {grade}')
        elif score == -1:
            loop = False
        else:
            print('Score error, enter again.')
        print()
    print('Exit Program...')


def checkGrade(score):
    grade = ''
    if score >= 80:
        grade = 'A'
    elif score >= 75:
        grade = 'B+'
    elif score >= 70:
        grade = 'B'
    elif score >= 65:
        grade = 'C+'
    elif score >= 60:
        grade = 'C'
    elif score >= 55:
        grade = 'D+'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'
    return(grade)


main()