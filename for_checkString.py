S = input('Enter string : ')
if S != '':
    count1 = count2 = count3 = count4 = 0
    
    for c in S:
        if c.islower():
            count1 += 1
        elif c.isupper():
            count2 += 1
        elif c.isdigit():
            count3 += 1
        else:
            count4 += 1
    
    print('Your string enter :', S)
    print(f'Lower letter : {count1}')
    print(f'Upper letter : {count2}')
    print(f'Digit number : {count3}')
    print(f'Special letter : {count4}')
else:
    print('String is empty!')