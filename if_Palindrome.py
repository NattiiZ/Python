palin = int(input('Enter integer number (4 Digit) : '))
if (palin<1000) or (palin>9999):
    print("Enter integer number \"4 Digit\" only!")
else:
    d1 = palin % 10
    digit = palin // 10
    d2 = digit % 10
    digit = digit // 10
    d3 = digit % 10
    digit = digit // 10
    d4 = digit % 10
    digit = digit // 10

    if (d4==d1) and (d3==d2):
        print(f'{palin} is Palindrome')
    else:
        print(f'{palin} is not Palindrome')