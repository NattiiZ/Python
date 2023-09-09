num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))
Max = 0

print()
if num1 > num2:
    if num1 > num3:
        Max = num1
    else:
        Max = num3
else:
    if num2 > num3:
        Max = num2
    else:
        Max = num3

print(f"Maximum number of {num1}, {num2}, {num3} = {Max}")

