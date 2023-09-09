loop = True
empty = False
headText = '| Program Calculate Grade Point Average |'
head = ('=')
size1 = (len(headText))
Sname = ''
Sscore = ''
text = ''
maxLen = 0
Tpoint = 0


while loop:
    print(head*size1)
    print(headText.center(size1))
    print(head*size1)

    print('- Input Data -')
    for i in range(1,6):
        Sub = input(f'Enter subject name({i}) : ')
        Score = input(f'Enter subject score({i}) : ')
        if Score == '' or Sub == '':
            print('\nSubject name or Score is empty.')
            empty = True
            break
        else:
            Score = float(Score)

            if Score < 50:
                grade = 'F'
                point = 0*3.0
            elif Score < 60:
                grade = 'D'
                point = 1*3.0
            elif Score < 70:
                grade = 'C'
                point = 2*3.0
            elif Score < 80:
                grade = 'B'
                point = 3*3.0
            elif Score <= 100:
                grade = 'A'
                point = 4*3.0
            else:
                print('Score is over!')
                break
        
        Score = str(Score)
        result = (f'{i}'.rjust(3) + ('  ')+Sub.ljust(22) + ('  ')+Score.rjust(5) + grade.rjust(5) + str(point).rjust(8))
        text += result + '\n'
        Tpoint += point

        for k in range(0,5):
            if len(result) > maxLen:
                maxLen = len(result)
        
        print()
    loop = False

if empty != True:
    size2 = maxLen+2
    print('Grade Point Average(GPA) Report'.center(size2))   
    print(head*size2)
    print('No.'.rjust(4) + ' Subject Name'.ljust(12) + ((' ')*13) + 'Mark' + 'Grade'.rjust(7) + ' Points')
    print(head*size2)
    print(text)
    print(head*size2)
    print('Total Points : ', Tpoint)
    print('Total Credits :', i*3)
    print('Grade Point Average(GPA) : %.2f' % (Tpoint/(i*3)))