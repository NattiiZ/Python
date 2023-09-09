num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))
num4 = int(input('Enter number 4 : '))
num5 = int(input('Enter number 5 : '))

Max = 0
if Max < num1:
    Max = num1
elif Max < num2:
    Max = num2
elif Max < num3:
    Max = num3
elif Max < num4:
    Max = num4
elif Max < num5:
    Max = num5
else:
    Max ='All equal!'

print()
print(f'Your enter number {num1}, {num2}, {num3}, {num4}, {num5}')
print('Maximum number is',Max)