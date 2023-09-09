menuStr = 'Main menu\n-----------------\n1. Exercise 1\n2. Exercise 2\n'
menuStr += '3. Exercise 3\n4. Exit\nSelect choice : '
main = True

while main:
    choice = input(menuStr)
    if choice == '1':
        print('-------- Program Find Maximun Digit --------\n')
        loop = True

        while loop:
            numStr = input('Enter integer number (0-Exit) : ')

            if numStr == 0:
                loop = False
            else:
                maxNum = 0
                # for i in range(len(numStr)):
                #     digitStr = numStr[i]
                #     digit = int(digitStr)
                #     if digit > maxNum:
                #         maxNum = digit

                # for digitStr in numStr:
                #     digit = int(digitStr)
                #     if digit > maxNum:
                #         maxNum = digit

                num = int(numStr)
                while num > 0:
                    digit = num % 10
                    num = num // 10
                    if digit > maxNum:
                        maxNum = digit

                print(f'Maximun Digit of integer number {numStr} = {maxNum}')

        # print('Exit Program')
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        main = False
print('Exit Program')