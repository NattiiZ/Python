total = 0
n = 0

def main():
    enterData()
    print('Total number :', total)
    print('Average value :', total/n)


def enterData():
    global total, n
    total = 0
    n = 0
    num = 0
    while (num!=-1):
        num = int(input(f'Enter value {n+1} : '))
        if (num!=-1):
            total += num
            n += 1


main()