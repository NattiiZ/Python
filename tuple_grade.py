def main():
    loop = True
    while loop:
        grade = input('Enter grade (Q-Exit) : ')
        grade = grade.upper()
        if grade == 'Q':
            loop = False
        else:
            value = checkGrade(grade)
            print(f'Score value of {grade} is {value}\n')
    
    print('Exit Program')
    print()


def checkGrade(grade):
    Grades = ('A', 'B', 'C', 'D', 'F')
    Values = (4, 3, 2, 1, 0)
    for i in range(len(Grades)):
        if grade == Grades[i]:
            return(Values[i])


main()