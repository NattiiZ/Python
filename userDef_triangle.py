def displayTriangle(num, ch):
    for n in range(num+1):
        message = ''
        for m in range(n):
            message += ch
        print(message)


print('Program displat triangle.')
num = int(input('Enter number of line : '))
ch = input('Enter character : ')
displayTriangle(num, ch)