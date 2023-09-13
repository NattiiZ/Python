def sumNumber(End):
    sum = 0;
    for n in range(1, End+1):
        sum += n
    print(f'Sum of 1 - {End} = {sum}')


print('Program sum 1 - n used function.')
num = int(input('Enter number : '))
sumNumber(num)