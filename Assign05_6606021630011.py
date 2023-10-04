from random import randint


def main():
    amount = int(input('Enter number student chairman : '))
    
    notVote=500; votePercent=0.0
    Number, voteTotal = VoteSim(amount)
    notVote -= voteTotal

    Display(voteTotal, notVote, Number, amount, votePercent)


def Percent(number, max):
    percent = (number/max)*100


    return percent


def VoteSim(amount):

    Number = [0]*(amount+1)
    voteTotal=0

    for i in range(500):
        vote = randint(0, amount)
        Number[vote]+=1

    for i in range(1, amount+1):
        voteTotal += Number[i]


    return (Number, voteTotal)

        
def Display(voteTotal, notVote, Number, amount, votePercent):
    print()
    print('Number of right student : 500')
    print(f'Number of Votes : {voteTotal} = %.2f%c' %(Percent(voteTotal, 500), '%'))
    print(f'Number of not Votes : {notVote} = %.2f%c' %(Percent(notVote, 500), '%'))

    print('\nResult of election chairman')
    print('-'*27)
    print(' No.' + f'Votes'.rjust(10) + f'Percent(%)'.rjust(14))
    print('-'*27)

    for i in range(1, amount+1):
        votePercent += Percent(Number[i], voteTotal)
        print(f'%3d. %8d  %10.2f' %(i, Number[i], Percent(Number[i], voteTotal)))

    print('-'*27)
    print(f'Total %7d %11.2f' %(voteTotal, votePercent))
        

main()