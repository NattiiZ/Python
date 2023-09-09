print('>> Program Fin Maximum Value <<\n')

value = int(input('Enter number of value (3-10) : '))
if value < 3:
    value = 3
elif value > 10:
    value = 10
print(f'\nProgram get value {value} numbers.')

loop = True
Max = 0
numStr = ''

while loop:
    for i in range(1, value+1):
        number = int(input(f'Enter value number #{i} : '))
        if Max < number:
            Max = number

        numStr += str(number)
        if i < value:
            numStr += ', '

    loop = False

print()
print(f'Your enter number : {numStr}')
print(f'Maximum value number is {Max}')
print('Exit Program')