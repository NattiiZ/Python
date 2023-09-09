number = int(input('Enter line number : '))
choice = input("Enter type (1-4): ")


if choice == '1':
    for row in range(1, number+1):
        for col in range(1, number+2-row):
            print('*',end='')
        print()

elif choice == '2':
    for row in range(1, number+1):
        for col in range(1, number+2-row):
            print('*',end='')
        print()

elif choice == '3':
    for row in range(1, number+1):
        for col in range(1, number+1):
            if col >= row:
                print('*',end='')
            else:
                print(' ',end='')
        print()

elif choice == '4':
    for row in range(1, number+1):
        for col in range(1, number+1):
            if col > number-row:
                print('*',end='')
            else:
                print(' ',end='')
        print()