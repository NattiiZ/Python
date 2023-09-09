tenBase = int(input('Enter Ten base number (1-15): '))


if (tenBase < 1) or (tenBase > 15):
    print("Number is not 1-15!")
else:
    d1 = tenBase % 2
    d1x = tenBase // 2
    d2 = d1x % 2
    d2x = d1x // 2
    d3 = d2x % 2
    d3x = d2x // 2
    d4 = d3x % 2
    d4x = d3x // 2


    binary = (str(d4)+ str(d3) + str(d2) + str(d1))
    print(tenBase, 'Convert to Binary =', binary)