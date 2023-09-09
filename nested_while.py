number = int(input('Enter line number : '))

row = 1
while row <= number:
    col = 1
    while col <= number:
        if col > number-row:
            print('*',end='')
        else:
            print(' ',end='')
        col += 1
    
    print()
    row += 1