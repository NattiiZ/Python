num = int(input('Enter number : '))

for n in range(1, num+1):
    if n % 2 == 0:
        print(f'{n} is even number')
    else:
        print(f'{n} is odd number')