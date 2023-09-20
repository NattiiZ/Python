from random import randint

def main():
    student = int(input('Enter number of student : '))
    subject = int(input('Enter number of subject : '))
    
    Scores = genData(student, subject)
    displayData(Scores,subject)    


def genData(std, sub):
    scores = []
    for r in range(std):
        scores.append([])
        for c in range(sub):
            scores[r].append(randint(0, 100))
    return scores


def displayData(scores,sub):
    n = 1
    for score in (scores):
        print(f'| Student %2d ' %n, end='| = ')
        for s in (score):
            print(f'| %3s ' %s, end='')
        print('| ', end='')
        print(f'%3.1f' %(round(sum(score)/sub,1)), end='')
        print(' | ', end='')
        print(f'%3d' %(max(score)), end='')
        print(' | ', end='')
        print(f'%3d' %(min(score)), end='')
        print(' |')
        n += 1


main()