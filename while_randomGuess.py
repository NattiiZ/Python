import random


print('======== guess the number ========\n')
loop = True
ans = random.randint(1,99)
# print(ans)


while loop:
    guess = int(input('Enter the number to guess : '))
    if guess < ans:
        print(f'- {guess} is too little.')
    elif guess > ans:
        print(f'- {guess} is too much.')
    else:
        print(f'- {guess} is correct!')
        loop = False
    print()