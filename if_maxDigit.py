numInt = int(input('Enter integer number (4 Digit) : '))
if (numInt>9999) or (numInt<1000):
    print("Enter integer number \"4 Digit\" only!")
else:
    # d1 = numInt % 10
    # digit = numInt // 10
    # d2 = digit % 10
    # digit = digit // 10
    # d3 = digit % 10
    # digit = digit // 10
    # d4 = digit % 10
    # # digit = digit // 10

    maxNum = 0

    # Case 1 -------------

    # if maxNum < d1:
    #     maxNum = d1
    # if maxNum < d2:
    #     maxNum = d2
    # if maxNum < d3:
    #     maxNum = d3
    # if maxNum < d4:
    #     maxNum = d4


    # Case 2 -------------

    # digit = numInt % 10
    # if maxNum < digit:
    #     maxNum = digit
    # numInt = numInt // 10

    # digit = numInt % 10
    # if maxNum < digit:
    #     maxNum = digit
    # numInt = numInt // 10

    # digit = numInt % 10
    # if maxNum < digit:
    #     maxNum = digit
    # numInt = numInt // 10

    # digit = numInt % 10
    # if maxNum < digit:
    #     maxNum = digit
    # numInt = numInt // 10


    # Case 3 -------------

    for i in range(4):
        digit = numInt % 10
        if maxNum < digit:
            maxNum = digit
        numInt = numInt // 10


    print(f'Maximun Digit of integer number = {maxNum}')

    # print(f'Maximun Digit of integer number {numInt} = {maxNum}')