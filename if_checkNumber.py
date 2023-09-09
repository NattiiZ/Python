num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))
Max = num1

print()
# if Max < num1:
#     Max = num1
if Max < num2:
    Max = num2
if Max < num3:
    Max = num3

print("Maximum number of %d, %d, %d = %d" %(num1, num2, num3, Max))