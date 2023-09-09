numInt = int(input('Enter integer number (1-9999) : '))

if numInt <= 0 or numInt > 9999:
    print('Enter number 1-9999 Only!')
else:
    print("\n||\n\/")

    # num1 = numInt//1000
    # num2 = (numInt-(num1*1000))//100
    # num3 = (numInt-((num1*1000)+(num2*100)))//10
    # num4 = (numInt-((num1*1000)+(num2*100)+(num3*10)))
    d1 = numInt % 10
    numInt = numInt // 10
    d2 = numInt % 10
    numInt = numInt // 10
    d3 = numInt % 10
    numInt = numInt // 10
    d4 = numInt % 10
    numInt = numInt // 10

    print()
    # print(num1)
    # print(num2)
    # print(num3)
    # print(num4)
    print(d1)
    print(d2)
    print(d3)
    print(d4)