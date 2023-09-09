print('======== Program Change Number to Text ========\n')
numInt = int(input('Enter integer number : '))
print('Number =', numInt)

numS = str(numInt)
digit = ''
text =''


for i in range(0,len(numS)):
    digit = numS[i]
    if digit == '1':
        text = 'One'
    elif digit == '2':
        text = 'Two'
    elif digit == '3':
        text = 'Three'
    elif digit == '4':
        text = 'Four'
    elif digit == '5':
        text = 'Five'
    elif digit == '6':
        text = 'Six'
    elif digit == '7':
        text = 'Seven'
    elif digit == '8':
        text = 'Eight'
    elif digit == '9':
        text = 'Nine'
    else:
        text = 'Zero'
    print(text)