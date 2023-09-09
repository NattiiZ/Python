import time

thousand, fiHandred, hundred = 1000, 500, 100
amount = int(input('Enter the amount you want to withdraw : '))
warn = '** Minimum amount 100$ **'

if amount < 100:
    print()
    print(warn)
else:
    print('Wait . . .\n')
    time.sleep(1)

    thousand  = amount//thousand
    fiHandred = (amount-(thousand*1000))//500
    hundred   = (amount-((thousand*1000)+(fiHandred*500)))//100
    remain    = (amount-((thousand*1000)+(fiHandred*500)+(hundred*100)))

    print('1000$ : ', thousand)
    print('500$  : ', fiHandred)
    print('100$  : ', hundred)

    if (remain < 100 and remain != 0):  
        print('\n** Remainder', remain, "$ **")
        print(warn)