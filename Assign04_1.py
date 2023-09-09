loop = True

while loop:
    base = int(input('Enter number (1-12) : '))

    if (base<2) or (base>12):
        print('Number is not 1-12, try again.')
    else:    
        print()
        print('-'*60)
        print('Multiplication Table'.center(60))
        print('-'*60)

        for i in range(1,13):
            for k in range(0,4):
                result = (base+k)*i
                print(f'{base+k}'.rjust(2) + ' x ' + f'{i}'.rjust(2) + ' = ' + f'{result}'.rjust(3),end=' |')

            print()
    print()